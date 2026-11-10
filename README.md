<h1 align="center">🤖 <br>YouTube RAG-Based ChatBot</h1>

<p align="center">
A smart conversational assistant built with <strong>LangChain</strong> and <strong>Python</strong> that uses <strong>Retrieval-Augmented Generation (RAG)</strong> to answer questions accurately based on the content of selected YouTube videos.
</p>
<hr>

## 📌 Features

- **YouTube URL Processing:** Accepts YouTube video links from anywhere on the platform.
- **Transcript Extraction & Chunking:** Automatically fetches and processes video transcripts for context retrieval.
- **Multi-Query Retrieval:** Generates multiple query variations to retrieve the most relevant context blocks.
- **Accurate Responses:** Delivers targeted answers grounded directly in the video's content.

---

## 📁 Repository Structure

```text
├── .github/workflows/   # CI/CD workflows
├── Config/              # Configuration files & environment setups
├── RAG_Components/      # Vector stores, embeddings, and retrieval logic
├── middleware/          # Request handling and input validation
├── module/              # Core modules (e.g., YouTube processing)
├── utils/               # Utility scripts and helper functions
├── main.py              # Main application entry point
├── README.md            # Project documentation
└── .gitignore           # Git ignore rules

