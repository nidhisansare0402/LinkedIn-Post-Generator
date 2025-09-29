from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import re
from collections import Counter

load_dotenv()
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# Marathi stopwords in Roman script
marathi_stopwords = set([
    "ahe", "ani", "che", "mhanje", "va", "madhe", "saathi", "jo", "aplya",
    "ya", "tya", "aat", "karun", "te", "tumcha"
])

# English stopwords
english_stopwords = set([
    "the", "and", "is", "in", "to", "of", "a", "for", "on", "with", "at",
    "this", "that", "as", "are", "by", "an", "or", "be", "it", "from", "your"
])

def generate_linkedin_post(topic, language="English", tone="Professional", length="Medium"):
    """
    Generate a LinkedIn post.
    - For Minglish: always pure Roman-script Marathi, no Hindi/English.
    """
    if language.lower() == "minglish":
        prompt = f"""
        Write a LinkedIn post about '{topic}' in Roman-script Marathi.
        - Do NOT include Hindi, English, or other languages.
        - Keep sentences natural, flowing, and professional.
        - Tone: {tone}, Length: {length}.
        """
    else:
        prompt = f"""
        Write a LinkedIn post about '{topic}' in {language}.
        Tone: {tone}, Length: {length}.
        Make it professional and suitable for LinkedIn.
        """

    response = llm.invoke(prompt)
    return response.content.strip()


def generate_hashtags(post_text: str, language="English", max_hashtags: int = 5) -> list:
    """
    Generate hashtags from the post text.
    - Minglish: exclude Marathi stopwords
    - English/Hinglish: exclude common stopwords
    - Picks meaningful content words for hashtags
    """
    post_text = post_text.lower()
    words = re.findall(r'\b\w+\b', post_text)

    if language.lower() == "minglish":
        words = [w for w in words if w not in marathi_stopwords and len(w) > 2]
    else:
        words = [w for w in words if w not in english_stopwords and len(w) > 2]

    if not words:
        return []

    word_counts = Counter(words)
    hashtags = [f"#{word}" for word, _ in word_counts.most_common(max_hashtags)]
    return hashtags
