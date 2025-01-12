from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_chroma import Chroma  # Updated import
from langchain_openai import ChatOpenAI
import os, openai
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatInterface:
    def __init__(self, db_dir: str):
        # Use the updated HuggingFaceEmbeddings
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # Use the updated Chroma
        self.vectorstore = Chroma(
            persist_directory=db_dir,
            embedding_function=self.embeddings
        )
        
        # Initialize ChatOpenAI
        self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

        
    def ask_question(self, question: str) -> str:
    # Get relevant chunks directly
        relevant_chunks = self.vectorstore.similarity_search(question, k=3)
        context = "\n\n".join(doc.page_content for doc in relevant_chunks)

        # Construct the system and user messages for GPT
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer questions. "
                                        "If the answer cannot be found in the context, explicitly say so."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
        ]

        # Call the OpenAI API directly
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # Use the model you want
                messages=messages,
                max_tokens=1500,         # Adjust as needed
                temperature=0         # Adjust for creative vs. deterministic responses
            )
            # Extract and return the response text
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            return "An error occurred. Please try again later."