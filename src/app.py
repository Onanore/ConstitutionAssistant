import streamlit as st
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from database import *
from embedding import get_embedding

st.set_page_config(page_title="Ollama Chatbot", layout="wide")

st.title("🤖 Local Chatbot with Ollama")
st.markdown("Upload the file and ask questions based on it.")

if "messages" not in st.session_state:
    st.session_state.messages = []

Ollama_model = st.sidebar.selectbox("Model: ",["deepseek-r1:1.5b", "deepseek-r1"])
temperature = st.sidebar.slider("temperature", 0.0, 1.0, 0.3)
uploaded_file = st.sidebar.file_uploader("Attach TXT file", type=["txt"])

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

if uploaded_file:
    documents = load_documents(uploaded_file, uploaded_file.name)
    chunks = split_documents(documents)
    add_to_chroma(chunks)
    st.success("File is uploaded!")


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = Ollama(model=Ollama_model, temperature = temperature, )
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text


prompt = st.chat_input("Question...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    answer = query_rag(prompt)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)