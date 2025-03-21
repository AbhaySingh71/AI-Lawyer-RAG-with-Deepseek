
<body>
    <h1>⚖️ AI Lawyer - RAG with DeepSeek R1</h1>
     <p>An AI-powered legal chatbot that leverages Retrieval-Augmented Generation (RAG) with <strong>DeepSeek R1</strong> and <strong>Ollama</strong> for advanced legal reasoning.</p>
    <p>This chatbot is designed to assist users in understanding complex legal documents, retrieving relevant case laws, and providing structured legal insights. By integrating DeepSeek R1, a sophisticated reasoning model, with the RAG framework, AI Lawyer ensures that responses are grounded in factual legal texts, reducing hallucinations and enhancing reliability. The chatbot can process large legal documents, break them down into meaningful sections, and retrieve the most pertinent information to answer user queries accurately.</p>
    
   <h2> Features</h2>
    <ul>
        <li>📂 Upload and analyze legal documents (PDFs)</li>
        <li>🔍 Retrieve relevant legal information using FAISS vector database</li>
        <li>🤖 Answer legal questions using DeepSeek R1 with Groq</li>
        <li>📜 Summarize legal documents</li>
        <li>📄 Generate downloadable AI-generated legal reports</li>
    </ul>
    
  <h2>📁 Project Structure</h2>
    <pre>
    ├── frontend.py          # Streamlit UI for AI Lawyer
    ├── rag_pipeline.py      # Retrieval-Augmented Generation pipeline
    ├── vector_database.py   # FAISS-based vector database
    ├── requirements.txt     # Python dependencies
    └── README.md            # Project documentation
    </pre>
    
  <h2>🛠️ Technologies Used</h2>
    <ul>
        <li><strong>DeepSeek R1</strong> - AI model for complex reasoning</li>
        <li><strong>Ollama</strong> - Local LLM hosting</li>
        <li><strong>LangChain</strong> - AI framework for LLM applications</li>
        <li><strong>Streamlit</strong> - Frontend UI for chatbot</li>
        <li><strong>FAISS</strong> - Vector search for document retrieval</li>
        <li><strong>pdfplumber</strong> - PDF document processing</li>
    </ul>
    
   <h2>⚙️ Installation & Setup</h2>

<h3>1️⃣ Clone the Repository</h3>
<pre>
git clone https://github.com/AbhaySingh71/AI-Powered-Healthcare-Intelligence-System.git
cd AI-Powered-Healthcare-Intelligence-System
</pre>

<h3>2️⃣ Set Up the Virtual Environment</h3>
<pre>
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
</pre>

<h3>3️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>
    
  <h2>🚀 Usage</h2>
    <ol>
        <li>Run the Streamlit application:</li>
        <pre><code>streamlit run frontend.py</code></pre>
        <li>Upload a legal document (PDF)</li>
        <li>Ask legal questions and get AI-powered responses</li>
        <li>Download AI-generated legal reports</li>
    </ol>
    
   <h2>📜 How It Works</h2>
    <ol>
        <li><strong>Upload PDF:</strong> Documents are uploaded and processed.</li>
        <li><strong>Vector Database:</strong> FAISS indexes the document text.</li>
        <li><strong>Query Handling:</strong> AI retrieves relevant information.</li>
        <li><strong>LLM Response:</strong> DeepSeek R1 generates answers.</li>
        <li><strong>Report Generation:</strong> AI generates a downloadable PDF report.</li>
    </ol>
    
  <h2>🎯 Future Improvements</h2>
    <ul>
        <li>📝 Add support for multiple document formats (DOCX, TXT)</li>
        <li>⚡ Improve response speed and accuracy</li>
        <li>🔗 Integrate legal databases for richer context</li>
    </ul>
    
 <h2>📬 Contact Us</h2>
<p>Have questions or need support? Reach out to us at:</p>
<ul>
  <li>📧 <a href="mailto:abhaysingh71711@gmail.com">abhaysingh71711@gmail.com</a></li>
</ul>

---

<h2>🌐 Connect With Me</h2>
<p align="center">
  <a href="https://github.com/abhaysingh71711" target="_blank">🐙 GitHub</a> |
  <a href="https://linkedin.com/in/abhaysingh71711" target="_blank">🔗 LinkedIn</a> |
  <a href="https://twitter.com/abhaysingh71711" target="_blank">🐦 Twitter</a>
</p>
