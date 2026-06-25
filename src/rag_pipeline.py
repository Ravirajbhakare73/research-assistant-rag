import re

def get_section(chunks, keywords):

    collected_text = []
    capture = False

    for chunk in chunks:

        text = chunk.page_content.upper()

        if not capture and any(k.upper() in text for k in keywords):
            capture = True

        if capture:
            collected_text.append(chunk.page_content)

        if capture:
            if any(text.startswith(p) for p in
                   ["I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII."]):
                if not any(k.upper() in text for k in keywords):
                    break

            if any(end in text for end in ["REFERENCES", "ACKNOWLEDGMENT", "APPENDIX"]):
                break

    return "\n\n".join(collected_text).strip()


def route_query(query, chunks, db):

    query_lower = query.lower()

    if "abstract" in query_lower:
        return get_section(chunks, ["ABSTRACT"])

    elif "introduction" in query_lower:
        docs = db.similarity_search(
            "introduction background overview blockchain cryptography",
            k=6
        )
        return "\n\n".join([d.page_content for d in docs])

    elif "conclusion" in query_lower:
        docs = db.similarity_search(
            "conclusion summary future work discussion",
            k=5
        )
        return "\n\n".join([d.page_content for d in docs])

    elif re.search(r"figure\s*\d+", query_lower):

        fig_no = re.search(r"figure\s*(\d+)", query_lower).group(1)

        for chunk in chunks:
            if f"FIGURE {fig_no}" in chunk.page_content.upper():
                return chunk.page_content

        return "Figure not found."

    else:
        docs = db.similarity_search(query, k=5)
        return "\n\n".join([d.page_content for d in docs])


def generate_answer(query, context, llm):

    prompt = f"""
You are an expert research paper assistant specializing in academic and IEEE-style technical documents.

Your task is to answer the user's question ONLY using the provided context.

STRICT RULES:
- Use ONLY the given context. Do NOT use outside knowledge.
- If the answer is not present in the context, clearly say: "Not found in the provided document."
- Do not guess or generate false information.
- Keep the answer concise, technical, and research-oriented.
- Maintain IEEE-style academic tone.

CONTEXT:
{context}

QUESTION:
{query}

FINAL ANSWER:
"""

    response = llm.invoke(prompt)
    return response.content


def rag_pipeline(query, chunks, db, llm):

    context = route_query(query, chunks, db)
    answer = generate_answer(query, context, llm)

    return answer