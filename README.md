# Research Paper RAG Assistant

## Overview

This project is a Retrieval-Augmented Generation (RAG) system designed to help users interact with research papers (especially IEEE-style PDFs).  
It allows users to upload a PDF and ask questions like:

- Abstract
- Introduction
- Conclusion
- Figures
- General questions about the paper

The system retrieves relevant context from the document and uses a Large Language Model (Google Gemini) to generate accurate answers.

---

## Features

- Upload any research paper PDF
- Automatic text cleaning and filtering
- Smart document chunking
- FAISS vector database for fast retrieval
- HuggingFace embeddings (384-dimensional model)
- Google Gemini LLM integration
- Streamlit UI for interactive Q&A
- Section-aware retrieval (Abstract, Introduction, Conclusion, Figures)
- RAG-based answer generation

---

## Project Structure
