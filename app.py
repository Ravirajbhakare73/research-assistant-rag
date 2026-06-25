import streamlit as st
import tempfile
import os
from dotenv import load_dotenv

from src.pdf_loader import load_pdf
from src.text_splitter import filter_documents, split_chunks
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.llm import get_llm
from src.rag_pipeline import rag_pipeline

load_dotenv()

st.set_page_config(page_title=" Research Assistant", layout="wide")

st.title("Research Paper Assistant")

# ---------------- SIDEBAR UPLOAD ----------------
st.sidebar.header(" Upload PDF")

uploaded_file = st.sidebar.file_uploader("Upload your research paper", type="pdf")

# ---------------- SESSION STATE ----------------
if "initialized" not in st.session_state:
    st.session_state.initialized = False


def build_pipeline(pdf_path):

    documents = load_pdf(pdf_path)

    filtered_docs = filter_documents(documents)
    chunks = split_chunks(filtered_docs)

    embedding_model = get_embedding_model()
    db = create_vector_store(chunks, embedding_model)

    llm = get_llm()

    return chunks, db, llm


# ---------------- PROCESS PDF ----------------
if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success("PDF uploaded successfully!")

    with st.spinner("Processing document..."):

        chunks, db, llm = build_pipeline(tmp_path)

        st.session_state.chunks = chunks
        st.session_state.db = db
        st.session_state.llm = llm
        st.session_state.initialized = True

    st.success("Ready for Q&A!")


# ---------------- QUERY UI ----------------
query = st.text_input("Ask your question")

if query:

    if not st.session_state.initialized:
        st.warning("Please upload a PDF first!")
    else:
        answer = rag_pipeline(
            query,
            st.session_state.chunks,
            st.session_state.db,
            st.session_state.llm
        )

        st.markdown("###  Answer")
        st.write(answer)