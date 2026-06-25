from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embedding_model):

    db = FAISS.from_documents(chunks, embedding_model)
    return db


def save_vector_store(db, path="vector_store"):

    db.save_local(path)


def load_vector_store(path, embedding_model):

    db = FAISS.load_local(
        path,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return db