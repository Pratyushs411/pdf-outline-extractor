# 🧠 PDF Outline Extractor — Adobe Hackathon 2025 Submission

A simple yet powerful Python-based tool to extract **Table of Contents (ToC)** or **bookmarks** from PDF documents and output them in a structured **JSON** format.

Built as a submission for 1.(a) of **Adobe Hackathon 2025**.

---

## 🏗️ Build Command

```bash
docker build --platform linux/amd64 -t pratyushs411/pdf-outline-extractor:latest .
```

## 📁 Project Structure
```
pdf-outline-extractor/
├── app/
│   ├── extractor.py        # Main logic to extract PDF outline
│   ├── input/              # Folder for input PDFs
│   └── output/             # Output JSON files
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container configuration
└── README.md               
```
## 🛠️ Technologies Used

### 🐍 Python Libraries
**[PyMuPDF (fitz)]** – Fast PDF parsing for outlines and bookmarks.

**[pdfminer.six==20221105]** – Fine-grained PDF content extraction (for future heading detection or content-based parsing).

**[spaCy==3.7.2]** – NLP library used to detect heading patterns, if bookmarks are not available.

**[scikit-learn]** – For vectorization and classification if needed in text pattern detection or section inference.

**[os, json, re]** – Standard libraries for file management and formatting.

### 🐳 Docker
Ensures platform-agnostic builds.
Cross-compatible with amd64 and arm64 architecture.

## 🔧 How It Works

1.PDFs placed in: app/input/
2.Script reads outlines (bookmarks) using PyMuPDF.
3.Outputs JSON hierarchy of the table of contents into app/output/.

## 🚀 Run Instructions

### Option 1: Using Docker
```
docker build --platform linux/amd64 -t pratyushs411/pdf-outline-extractor:latest .

docker run --rm \
  -v $(pwd)/app/input:/app/input \
  -v $(pwd)/app/output:/app/output \
  pratyushs411/pdf-outline-extractor:latest
```

### Option 2: Local (Python only)
```
pip install -r requirements.txt
python app/extractor.py
```
## 📤 Sample Output (JSON)

```
[
  {
    "title": "Chapter 1",
    "page": 1,
    "children": [
      {
        "title": "Section 1.1",
        "page": 2
      }
    ]
  }
]

```

## Critical Constraints

**Execution Time:** ≤ 10 seconds for a 50-page PDF.  
**Model Size:** ≤ 200MB (if using ML models).  
**Network:** No internet access allowed during runtime execution.  
**Runtime:** Must run on CPU (amd64) with 8 CPUs and 16 GB RAM.  
**Architecture:** Must work on AMD64, not ARM-specific.  

## ⚠️ Limitations

Only works on PDFs with embedded outlines/bookmarks.

Does not currently infer structure from visual layout (future scope).



