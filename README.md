# Mental-Health-Support-RAG-Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about mental health conditions using a curated knowledge base, grounding every response in retrieved context rather than relying on the LLM's raw knowledge.

## How it works

1. **Data collection** — Mental health information is scraped from trusted sources using a Scrapy pipeline (`mental_health_chatbot/`), producing `data.json`.
2. **Indexing** — Source text is chunked and embedded with `sentence-transformers/all-MiniLM-L6-v2`, then indexed with FAISS for fast similarity search (built in `FinalProject.ipynb`, stored as `Data/index.faiss` and `Data/chunks_only.pkl`).
3. **Retrieval** — At query time, the user's question is embedded and the top-k most relevant chunks are retrieved via FAISS cosine similarity search.
4. **Generation** — Retrieved chunks are passed as context to Google's Gemini (`gemini-2.0-flash`), which generates a compassionate, context-grounded answer. If the question falls outside the knowledge base, the bot explicitly says so rather than guessing.
5. **Interface** — A Streamlit chat UI (`app.py`) handles conversation state and displays the exchange.

## Tech stack

- **Frontend/UI:** Streamlit
- **Embeddings:** `sentence-transformers` (`all-MiniLM-L6-v2`)
- **Vector search:** FAISS
- **LLM:** Google Gemini API (`gemini-2.0-flash`)
- **Data collection:** Scrapy
- **Language:** Python

## Project structure

```
├── Data/                     # FAISS index + serialized text chunks
├── mental_health_chatbot/    # Scrapy project for data collection
├── scrapy.cfg
├── data.json                 # Raw scraped mental health data
├── FinalProject.ipynb        # Data processing, embedding & index-building notebook
├── app.py                    # Streamlit RAG chatbot application
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/isis-ashraf/Mental-Health-Support-RAG-Chatbot.git
   cd Mental-Health-Support-RAG-Chatbot
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project root with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Limitations

- Not a substitute for professional medical or psychological advice.
- Answers are only as good as the knowledge base — questions outside the scraped source material are declined rather than hallucinated.
