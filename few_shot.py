import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            # Collect unique tags
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length: str, language: str, tag: str):
        """
        Filter posts by length, language, and tag.
        Automatically treats Minglish posts as strict Roman-script Marathi.
        """
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &
            (self.df['length'] == length)
        ]

        if language.lower() == "minglish":
            # Keep only posts marked as Minglish
            df_filtered = df_filtered[df_filtered['language'] == "Minglish"]
        else:
            df_filtered = df_filtered[df_filtered['language'] == language]

        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count: int) -> str:
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags or []
