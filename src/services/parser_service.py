import fitz

class ParserService:
    def __init__(self, parser):
        self.parser = parser

    def parse(self, pdf_content):
        resume_text = ""
        with fitz.open(stream=pdf_content, filetype="pdf") as doc:
            for page in doc:
                resume_text += page.get_text()
        return ...