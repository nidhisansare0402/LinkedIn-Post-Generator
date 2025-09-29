# LinkedIn-Post-Generator
A Python project that generates professional LinkedIn posts in Minglish, Hinglish, and English using LLMs. It produces context-aware content with relevant hashtags, showcasing skills in NLP, LangChain, and API integration.

---

## Features

- Generate LinkedIn posts in **Minglish, Hinglish, and English**.
- Automatically suggest **relevant hashtags**.
- Leverages **LLM** for natural, human-like content.
- Modular, easy-to-customize design.
- Supports JSON-based input/output for post data.

---
## Project Interface

Here’s a snapshot of the LinkedIn Post Generator in action:
<img width="940" height="453" alt="image" src="https://github.com/user-attachments/assets/a774d9d4-a559-4765-9f9c-82500166d64a" />
---

## Tech Stack

- **Python 3.11+**
- **LangChain** – for LLM integration  
- **Groq API (ChatGroq)** – for fast inference  
- **Streamlit** – for building a simple UI   
- **dotenv** – for managing environment variables  
- **JSON** – for post storage and processing  

---

## 📂 Project Structure

```text
LinkedIn-Post-Generator/
│
├─ main1.py            # Entry point for running the project
├─ llm_helper.py       # Handles LLM API integration
├─ post_generator.py   # Core logic for generating LinkedIn posts
├─ few_shot.py         # Contains few-shot learning examples/prompts
├─ preprocess.py       # Preprocessing raw data before generation
├─ processed_posts/    # Folder to store processed posts
├─ raw_posts.json      # Sample input data
├─ .env                # API keys and environment variables
└─ README.md           # Project documentation

