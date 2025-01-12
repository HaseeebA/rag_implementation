from src.document_converter import DocumentConverter
from src.embedding_creator import EmbeddingCreator
from src.chat_interface import ChatInterface
if __name__ == "__main__":
    # Convert documents
    converter = DocumentConverter("documents", "markdown")
    converter.process_documents()
    
    # Create embeddings
    creator = EmbeddingCreator("markdown", "chroma_db")
    creator.create_embeddings()
    
    # Chat interface
    chat = ChatInterface("chroma_db")
    
    while True:
        question = input("\nEnter your question (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        
        answer = chat.ask_question(question)
        print(f"\nAnswer: {answer}")