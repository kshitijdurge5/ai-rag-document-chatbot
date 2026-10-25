import streamlit as st
from portfolio_visuals import render_visuals
from pathlib import Path

def answer_question(question: str, text: str) -> dict:
    """Minimal baseline: returns matching text lines, not a full semantic RAG pipeline."""
    terms = {t.strip(".,?!:;").lower() for t in question.split() if len(t) > 3}
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    matches = [line for line in lines if any(term in line.lower() for term in terms)]
    return {"answer": "\n".join(matches[:5]) if matches else "No matching passage found in the supplied text.", "sources": [f"Text line {i+1}" for i,line in enumerate(lines) if line in matches[:5]]}

st.set_page_config(page_title="Document Q&A", page_icon="ðŸ“š")
render_visuals('02_rag_document_chatbot')
st.title("Document Q&A â€” Retrieval Starter")
st.warning("This MVP uses keyword matching. It is not yet embedding-based RAG and does not accept arbitrary PDF uploads.")
doc = st.text_area("Paste sample document text", height=220)
q = st.text_input("Ask a question")
if st.button("Find passages"):
    if not doc.strip() or not q.strip():
        st.warning("Provide document text and a question.")
    else:
        result = answer_question(q, doc)
        st.write(result["answer"])
        st.caption("Evidence locations: " + ", ".join(result["sources"]))

