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
```
---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- Git

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mafimashrafi/RAG_Based_ChatBot.git
   cd RAG_Based_ChatBot
   ```

2. **Create and activate a virtual environment:**

   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add your required API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
---

## 💡 Usage

Run the main script to start the chatbot:

```bash
python main.py
```

Follow the prompts to enter a YouTube video URL and ask questions regarding its content.

---

## 🛠️ Built With

- [**LangChain**](https://www.langchain.com/) – Framework for developing applications powered by language models.
- **Python** – Primary programming language.
- **Vector Database / Embeddings** – For semantic document indexing and retrieval.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.
