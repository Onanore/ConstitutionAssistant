# ConstitutionAssistant

A locally-hosted chatbot powered by Ollama that implements Retrieval-Augmented Generation (RAG) to answer questions based on uploaded text documents. The application uses Streamlit for the web interface, LangChain for document processing, and Chroma as the vector database.

## Features

- Upload and process text documents
- Interactive chat interface
- Document chunking and embeddings generation
- Similarity search using ChromaDB
- Configurable LLM parameters (temperature, model selection)
- Local execution without cloud dependencies

## Installation

1. First, ensure you have [Ollama](https://ollama.ai/) installed on your system.

2. Clone this repository:
```bash
git clone https://github.com/Onanore/ConstitutionAssistant
cd ConstitutionAssistant
```

3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

5. Pull the required Ollama models:
```bash
ollama pull deepseek-r1:1.5b
ollama pull deepseek-r1
ollama pull nomic-embed-text
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the displayed URL (typically http://localhost:8501)

3. In the sidebar:
   - Select your preferred model (deepseek-r1:1.5b or deepseek-r1)
   - Adjust the temperature setting (0.0 to 1.0)
   - Upload a text file using the file uploader

4. Start chatting! Ask questions about your uploaded document in the chat input field.

## Example Interaction

1. Upload a text document containing information you want to query
2. Wait for the "File is uploaded!" success message
3. Ask questions in the chat input, for example:
   - "Can you summarize the key points from article X?"
   - "What does the document say about Y?"

## Project Structure

```
.
streamlit-chat-app/
├── README.md
├── requirements.txt
├── License
└── src/
     ├── app.py
     ├── database.py 
     ├── embedding.py
     └── chroma_db/
```
