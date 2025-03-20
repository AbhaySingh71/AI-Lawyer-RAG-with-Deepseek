import streamlit as st
import time
from vector_database import index_pdf, upload_pdf
from rag_pipeline import answer_query, retrieve_docs, llm_model, summarize_document, generate_report

# --- Page Configuration ---
st.set_page_config(page_title="AI Lawyer", page_icon="⚖️", layout="centered")

# --- Custom Styling for Dark Mode ---
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #E0E0E0;
            font-family: Arial, sans-serif;
        }
        .stTextArea textarea {
            font-size: 16px;
            border-radius: 10px;
            padding: 12px;
            border: 2px solid #4CAF50;
            background-color: #1E1E1E;
            color: white;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 0px 4px 10px rgba(76, 175, 80, 0.3);
        }
        .stButton button:hover {
            background-color: #388E3C;
        }
        .stChatMessage {
            border-radius: 12px;
            padding: 15px;
            margin: 10px 0;
            background-color: #1E1E1E;
            box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.1);
            color: #E0E0E0;
        }
        .uploaded-file {
            color: #81C784;
            font-weight: bold;
            font-size: 16px;
        }
        .summary-box {
            background-color: #1E1E1E;
            padding: 15px;
            border-left: 5px solid #4CAF50;
            color: #E0E0E0;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(76, 175, 80, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "user_queries" not in st.session_state:
    st.session_state.user_queries = []
if "ai_responses" not in st.session_state:
    st.session_state.ai_responses = []

# --- Upload PDF ---
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>⚖️ AI Lawyer Chatbot</h1>
    <p style='text-align: center; font-size: 18px; color: #E0E0E0;'>
        A RAG-based legal reasoning chatbot using DeepSeek and Ollama.
        Upload a legal document (PDF) and get AI-powered answers.
    </p>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Upload a legal document (PDF)", type="pdf", accept_multiple_files=False)

from vector_database import index_pdf

if uploaded_file:
    st.success(f"📄 Uploaded: {uploaded_file.name}")

    # Index the uploaded document
    file_path = upload_pdf(uploaded_file)  # Save file
    index_pdf(file_path)  # Index file in FAISS

    # Summarization Feature
    if st.button("📜 Summarize Document"):
        with st.spinner("🔍 Generating summary..."):
            time.sleep(1)
            retrieved_docs = retrieve_docs("Summarize this document", uploaded_file.name)
            if not retrieved_docs:
                st.error("❌ No content retrieved. Try re-uploading the document.")
                print("Debug: No documents retrieved.")
            else:
                print("Debug: Retrieved documents:", retrieved_docs)
                summary = summarize_document(retrieved_docs)
                st.markdown("### 📝 Document Summary:")
                st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

# --- Chat Interface ---
user_query = st.text_area("💬 Ask your legal question:", height=120, placeholder="Type your question here...")

if st.button("🔍 Ask AI Lawyer"):
    if uploaded_file:
        with st.spinner("⚡ Analyzing document and generating response..."):
            time.sleep(1)
            st.chat_message("user").write(user_query)
            
            retrieved_docs = retrieve_docs(user_query, uploaded_file.name)
            response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
            
            st.chat_message("AI Lawyer").write(response)
            
            # Store conversation in session state
            st.session_state.user_queries.append(user_query)
            st.session_state.ai_responses.append(response)
    else:
        st.error("❌ Please upload a valid PDF file before asking a question!")

# --- Download Report Feature ---
if st.session_state.user_queries and st.session_state.ai_responses:
    if st.button("📥 Download Report"):
        report_path = generate_report(st.session_state.user_queries, st.session_state.ai_responses)
        with open(report_path, "rb") as file:
            st.download_button(label="📄 Download AI Lawyer Report", data=file, file_name="AI_Lawyer_Report.pdf", mime="application/pdf")