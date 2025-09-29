from llm_helper import generate_linkedin_post, llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length: str) -> str:
    if length == "Short":
        return "1 to 5 lines"
    elif length == "Medium":
        return "6 to 10 lines"
    else:
        return "11 to 15 lines"

def generate_post(length: str, language: str, tag: str, tone="Professional") -> str:
    """
    Generate a LinkedIn post.
    - Minglish: strict Roman-script Marathi with few-shot examples for natural flow.
    """
    if language.lower() == "minglish":
        examples = few_shot.get_filtered_posts(length, language, tag)
        example_texts = ""
        for i, post in enumerate(examples[:2]):
            example_texts += f"\nExample {i+1}: {post['text']}\n"

        prompt = f"""
        Generate a LinkedIn post in Roman-script Marathi about "{tag}".
        Tone: {tone}, Length: {get_length_str(length)}.
        STRICT RULES:
        - Do NOT include Hindi or English words.
        - Use only Marathi words in Roman letters.
        - Keep sentences natural, flowing, and professional for LinkedIn.
        {example_texts}
        Write a new post below (do NOT repeat examples):
        """
        response = llm.invoke(prompt)
        return response.content.strip()
    else:
        return generate_linkedin_post(
            topic=tag,
            language=language,
            tone=tone,
            length=length
        )
