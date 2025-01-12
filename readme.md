# Document RAG (Retrieval-Augmented Generation) Project

This project implements a simple RAG system that allows you to extract text from PDF and DOCX documents, convert them to markdown format, create embeddings, and query your documents using natural language.

## Clone Repository

```bash
git clone https://github.com/HaseeebA/rag_implementation.git
```

## Project Structure
```
rag_implementation/
├── .env                  # Environment variables
├── requirements.txt      # Project dependencies
├── documents/           # Store your PDF and DOCX files here
├── markdown/           # Converted markdown files
├── chroma_db/         # Vector database storage
├── main.py
└── src/
    ├── document_converter.py
    ├── embedding_creator.py
    └── chat_interface.py
```

## Setup Instructions

1. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Environment Setup**
Create a `.env` file in the project root and add your configuration:
```
OPENAI_API_KEY=your_api_key_here  # If using OpenAI
```

4. **Prepare Documents**
- Create a `documents` folder in the project root
- Place your PDF and DOCX files in the `documents` folder
- The system will automatically create a `markdown` folder for converted files

## Usage

1. **Document Preparation**
- Place all your documents (PDFs and DOCXs) in the `documents` folder
- The converter will automatically create similarly named markdown files in the `markdown` folder

2. **Run the System**
```bash
python main.py
```

The script will:
1. Convert all documents to markdown format
2. Create embeddings and store them in the ChromaDB database
3. Start an interactive chat interface

3. **Querying**
- Type your questions in natural language
- Type 'quit' to exit the system

## Customization

### Adjusting Chunk Size
In `src/embedding_creator.py`, you can modify the text splitting parameters:
```python
self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Adjust this value
    chunk_overlap=200,  # Adjust overlap between chunks
    length_function=len
)
```

### Modifying Number of Retrieved Results
In `src/chat_interface.py`, you can adjust the number of relevant chunks retrieved:
```python
relevant_chunks = self.vectorstore.similarity_search(question, k=3)  # Adjust k value
```

## Important Notes

1. **Document Support**
   - Supported formats: PDF (.pdf) and Word documents (.docx)
   - Make sure documents are text-based (OCR might be needed for scanned PDFs)

2. **Memory Usage**
   - Large documents will use more RAM during processing
   - Adjust chunk sizes if you experience memory issues

3. **Embeddings**
   - Using HuggingFace's all-MiniLM-L6-v2 model for embeddings (free and local)
   - Embeddings are stored locally in the chroma_db folder

## Troubleshooting

1. **Document Conversion Issues**
   - Ensure documents are not corrupted
   - Check file permissions
   - Verify documents contain extractable text

2. **Memory Issues**
   - Reduce chunk_size in embedding_creator.py
   - Process fewer documents at once

3. **Embedding Creation**
   - Ensure enough disk space for the database
   - Check write permissions for the chroma_db directory

## Example Usage

```python
# Example query
Q: "What are the main points discussed in chapter 1?"
A: [System will return relevant information from your documents]
```

## Directory Maintenance

- Regularly clean up the `markdown` and `chroma_db` folders if you want to start fresh
- Keep backups of your original documents
- Consider organizing documents in the `documents` folder by topic or date

## Future Improvements

1. Add support for more document formats
2. Implement document metadata tracking
3. Add batch processing for large document sets
4. Include document source in responses

## FAQs

**Q: How do I change the embedding model?**
A: Modify the model_name parameter in `embedding_creator.py`:
```python
self.embeddings = HuggingFaceEmbeddings(model_name="your-preferred-model")
```

**Q: Where is my data stored?**
A: Your data is stored locally:
- Original documents in `documents/`
- Converted text in `markdown/`
- Embeddings in `chroma_db/`

**Q: How can I optimize retrieval quality?**
A: You can:
- Adjust chunk sizes
- Modify overlap between chunks
- Change the number of retrieved chunks (k value)
- Experiment with different embedding models