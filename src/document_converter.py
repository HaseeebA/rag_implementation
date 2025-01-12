from pathlib import Path
from PyPDF2 import PdfReader
from docx import Document

class DocumentConverter:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def convert_pdf(self, file_path: Path) -> str:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
        return text
    
    def convert_docx(self, file_path: Path) -> str:
        doc = Document(file_path)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    
    def process_documents(self):
        for file_path in self.input_dir.glob('*.*'):
            if file_path.suffix.lower() in ['.pdf', '.docx']:
                print(f"Processing {file_path.name}")
                
                # Convert the document
                if file_path.suffix.lower() == '.pdf':
                    text = self.convert_pdf(file_path)
                else:
                    text = self.convert_docx(file_path)
                
                # Save as markdown
                output_path = self.output_dir / f"{file_path.stem}.md"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Created {output_path.name}")