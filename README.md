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

## Tech Stack

- **Python 3.11+**
- **LangChain** – for LLM integration  
- **Groq API (ChatGroq)** – for fast inference  
- **Streamlit** – for building a simple UI   
- **dotenv** – for managing environment variables  
- **JSON** – for post storage and processing  

---

## Project Structure

```text
LinkedIn-Post-Generator/
│
├─ llm_helper.py       # Handles LLM API integration
├─ main.py             # Entry point for generating posts
├─ processed_posts/    # Folder to store processed posts
├─ raw_posts.json      # Sample input data
├─ .env                # API keys and environment variables
└─ README.md           # Project documentation
