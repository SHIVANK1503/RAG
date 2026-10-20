# RAG (Retrieval-Augmented Generation) with LangChain

A hands-on, module-by-module walkthrough of the building blocks of a RAG pipeline using **LangChain**, **ChromaDB**, and **Google Gemini embeddings**.

---

## What is RAG?

Large Language Models only know what they were trained on. **Retrieval-Augmented Generation (RAG)** fixes this by fetching relevant information from your own data at query time and passing it to the LLM as context.

```
 Documents ──► Loaders ──► Text Splitters ──► Embeddings ──► Vector DB
                                                                │
 User Query ──► Embed Query ──► Retriever ◄─────────────────────┘
                                    │
                                    ▼
                          Relevant chunks + Query
                                    │
                                    ▼
                                   LLM ──► Answer
```

---

## Project Structure

```
.
├── 1_Document_loaders/
│   ├── books/
│   ├── cricket.txt
│   ├── csv_loader.py
│   ├── directory_loader.py
│   ├── dl-curriculum.pdf
│   ├── pdf_loader.py
│   ├── Social_Network_Ads.csv
│   ├── text_loader.py
│   └── webbase_loader.py
│
├── 2_Text_splitters/
│   ├── _notes.txt
│   ├── document_based_splitter.py
│   ├── length_based_splitting.py
│   ├── semantic_based_splitting.py
│   └── text_based_splitter.py
│
├── 3_Vector_DB/
│   ├── my-chroma-db/
│   └── vector_store.ipynb
│
├── 4_Retrievers/
│   ├── _notes.txt
│   └── retrievers.ipynb
│
├── 5_Tools/
│   └── _notes.text
│
├── 6_Agents/
│   ├── agents.text
│   └── AI_agents.ipynb
│
├── .env
├── .gitignore
└── requirements.txt
```

---

## Components

### 1. Document Loaders (`1_Document_loaders/`)
Load raw data from different sources into LangChain `Document` objects (`page_content` + `metadata`).

| File | Purpose |
|------|---------|
| `text_loader.py` | Load plain `.txt` files (e.g. `cricket.txt`) |
| `pdf_loader.py` | Load and parse PDFs (e.g. `dl-curriculum.pdf`) |
| `csv_loader.py` | Load rows from CSV files (e.g. `Social_Network_Ads.csv`) |
| `directory_loader.py` | Load many files at once from a folder (e.g. `books/`) |
| `webbase_loader.py` | Scrape and load content from web pages |

### 2. Text Splitters (`2_Text_splitters/`)
LLMs and embedding models have context limits, so large documents are broken into smaller chunks before embedding.

| File | Strategy |
|------|----------|
| `length_based_splitting.py` | Split by a fixed number of characters/tokens |
| `text_based_splitter.py` | Split on text structure (paragraphs, sentences, words) with overlap |
| `document_based_splitter.py` | Split based on document type/structure (e.g. code, markdown) |
| `semantic_based_splitting.py` | Split where the *meaning* changes, using embeddings |

See `_notes.txt` for notes on when to use each.

### 3. Vector Database (`3_Vector_DB/`)
Chunks are converted to embeddings (numerical vectors) and stored in **ChromaDB** for similarity search.

- `vector_store.ipynb`: create a vector store, add documents, and run similarity searches
- `my-chroma-db/`: persisted Chroma database (created via `persist_directory`)

### 4. Retrievers (`4_Retrievers/`)
Retrievers take a query and return the most relevant documents from the vector store.

- `retrievers.ipynb`: experiments with different retrieval strategies (similarity search, MMR, etc.)
- `_notes.txt`: notes on retriever types and trade-offs

### 5. Tools (`5_Tools/`)
Tools let an LLM call external functions (search, calculators, APIs, retrievers). Notes are in `_notes.text`.

### 6. Agents (`6_Agents/`)
Agents use an LLM to decide *which* tools to call and in what order to solve a task.

- `AI_agents.ipynb`: building agents that use tools
- `agents.text`: notes on agent concepts

---

## Tech Stack

- **Python 3.10+**
- [LangChain](https://python.langchain.com/) (`langchain`, `langchain-core`, `langchain-community`)
- [ChromaDB](https://www.trychroma.com/) via `langchain-chroma`
- [Google Gemini](https://ai.google.dev/) embeddings via `langchain-google-genai`

---

## Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Create and activate a virtual environment
```bash
python -m venv myenv

# Windows
myenv\Scripts\activate

# macOS / Linux
source myenv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

> `.env` is listed in `.gitignore`. Never commit your API keys.

### 5. Run the examples
- Python scripts: `python 1_Document_loaders/pdf_loader.py`
- Notebooks: open the `.ipynb` files in VS Code or Jupyter and run the cells in order.

---

## Quick Example

```python
from langchain_chroma import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

docs = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
]

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    collection_name="my_collection",
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})
print(retriever.invoke("What is Chroma?"))
```

---

## Troubleshooting

**`IndexError: list index out of range` in `Chroma.from_documents`**
The embedding call returned fewer vectors than the number of input texts. This happened with `gemini-embedding-2-preview` on some package versions. Fix: use the stable `gemini-embedding-001` model, or upgrade `langchain-google-genai`.

**Works in Google Colab but not locally**
Package versions usually differ. Compare with `pip list` in both environments and align them, then restart the kernel.

**Switching embedding models**
Vectors from different embedding models are not comparable. If you change models, delete the old Chroma collection (or `my-chroma-db/`) and re-embed your documents.

---

## Learning Path

1. Document Loaders
2. Text Splitters
3. Vector DB
4. Retrievers
5. Tools
6. Agents

---
