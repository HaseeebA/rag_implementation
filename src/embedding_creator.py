from pathlib import Path
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_chroma import Chroma  # Updated import
from langchain.text_splitter import RecursiveCharacterTextSplitter

class EmbeddingCreator:
    def __init__(self, markdown_dir: str, db_dir: str):
        load_dotenv()
        self.markdown_dir = Path(markdown_dir)
        self.db_dir = db_dir
        # Using a smaller, efficient model for embeddings
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=200,
            length_function=len
        )
    
    def create_embeddings(self):
        documents = []
        
        # Read all markdown files
        for file_path in self.markdown_dir.glob('*.md'):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                chunks = self.text_splitter.split_text(text)
                documents.extend(chunks)
        
        # Create and persist the vector store
        vectorstore = Chroma.from_texts(
            texts=documents,
            embedding=self.embeddings,
            persist_directory=self.db_dir
        )
        return vectorstore