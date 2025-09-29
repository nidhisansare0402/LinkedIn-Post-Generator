import json
from llm_helper import generate_hashtags


def process_posts(raw_file_path, processed_file_path=None):
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        enriched_posts = []

        for post in posts:
            metadata = extract_metadata(post['text'])
            post_hashtags = generate_hashtags(
                post['text'],
                language=metadata['language']
            )
            enriched_posts.append({**post, **metadata, "hashtags": post_hashtags})

    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        post['tags'] = [unified_tags.get(tag, tag) for tag in post['tags']]

    if processed_file_path:
        with open(processed_file_path, "w", encoding="utf-8") as outfile:
            json.dump(enriched_posts, outfile, indent=4)


def extract_metadata(post_text: str) -> dict:
    """
    Basic metadata extraction.
    Language detection:
    - ASCII-only text → English
    - Non-ASCII or mixed Roman script → Minglish
    """
    lines = post_text.split("\n")
    line_count = len(lines)

    # Simple language detection for Minglish
    if all(ord(c) < 128 for c in post_text):
        language = "English"
    else:
        # Treat any Roman-script Marathi as Minglish
        language = "Minglish"

    tags = []  # Placeholder; can use LLM to extract tags later
    return {"line_count": line_count, "language": language, "tags": tags}


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])
    return {tag: tag.title() for tag in unique_tags}
