import re
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def filter_documents(documents):

    filtered_documents = []

    for doc in documents:

        text = doc.page_content

        text = re.sub(r"Digital Object Identifier.*?\n", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\S+@\S+", "", text)
        text = re.sub(r"Received .*?current version .*?\.", "", text, flags=re.IGNORECASE | re.DOTALL)
        text = re.sub(r"This work is licensed under.*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\n\d{4,6}\n", "\n", text)

        if "REFERENCES" in text.upper():
            text = text[:text.upper().find("REFERENCES")]

        text = re.sub(r"\n{2,}", "\n", text)
        text = re.sub(r"[ \t]+", " ", text)

        filtered_documents.append(
            Document(
                page_content=text.strip(),
                metadata=doc.metadata
            )
        )

    print("Filtered Pages:", len(filtered_documents))
    return filtered_documents


def split_chunks(filtered_documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )

    chunks = splitter.split_documents(filtered_documents)

    print("Total Chunks:", len(chunks))
    return chunks