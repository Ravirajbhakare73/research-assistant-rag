# Research Paper RAG Assistant

## Overview

This project is a Retrieval-Augmented Generation (RAG) system built for interacting with IEEE-style research papers. It allows users to upload a PDF research paper and ask questions such as:

- Abstract
- Introduction
- Conclusion
- Figure-based queries
- General semantic questions

The system uses FAISS for vector storage, HuggingFace embeddings for text representation, and Google Gemini (LLM) for generating final answers.

---

## Features

- Upload and process any research paper (PDF)
- Automatic PDF cleaning (removes DOI, emails, metadata, references, etc.)
- Smart text chunking with overlap
- Semantic search using FAISS
- Section-based retrieval (Abstract, Introduction, Conclusion, Figures)
- LLM-based answer generation using Gemini API
- Streamlit web interface
- Fully modular architecture

---

## Project Structure

```
Project/

├── .vscode/
├── data/
│   └── paper_block.pdf
│
├── Notebook/
│   ├── vector_store/
│   │   ├── index.faiss
│   │   └── index.pkl
│   └── Trials.ipynb
│
├── src/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── llm.py
│   └── rag_pipeline.py
│
├── uploads/
├── vector_store/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── LICENSE
└── template.sh
```

---

## Installation

### 1. Clone the repository
```
git clone <your-repo-url>
cd research-assistant-rag
```

### 2. Create virtual environment
```
python -m venv venv
venv\Scripts\activate   (Windows)
source venv/bin/activate (Linux/Mac)
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

## How to Run

### Streamlit App

```
streamlit run app.py
```

---

## How It Works

### 1. PDF Loading
- PDF is loaded using PyPDFLoader

### 2. Cleaning
- Removes:
  - DOI
  - Emails
  - Page numbers
  - References
  - Copyright text

### 3. Chunking
- RecursiveCharacterTextSplitter splits text into overlapping chunks

### 4. Embeddings
- Uses HuggingFace sentence-transformers model (384-dimension)

### 5. Vector Store
- FAISS stores embeddings for fast similarity search

### 6. Retrieval Strategy
- Rule-based routing for:
  - Abstract
  - Introduction
  - Conclusion
  - Figures
- Semantic search for all other queries

### 7. LLM Generation
- Google Gemini generates final response using retrieved context

---

## Tech Stack

- Python 3.12
- Streamlit
- LangChain
- FAISS
- HuggingFace Transformers
- Sentence-Transformers
- Google Gemini API

---

## Example Queries

- What is the abstract?
- Explain introduction
- Give conclusion
- Show figure 2
- What is blockchain?
- Summarize the paper

---

## Notes

- Works with any IEEE-style PDF paper
- Chunk size and overlap can be tuned for better retrieval
- FAISS index can be reused for faster loading (future optimization)

---

## Future Improvements

- Add multi-document support
- Add caching for embeddings and FAISS index
- Add highlighting of answers in PDF
- Add citation-based responses

---

## Author

Built as a Research Assistant RAG system for academic document understanding.

---