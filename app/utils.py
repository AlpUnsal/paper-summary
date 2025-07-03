import pymupdf4llm
import os

def pdf_to_text(pdf_file: str = "") -> str:
    assert pdf_file != "" or os.path.isfile(pdf_file), "Please provide a valid file path"

    text = pymupdf4llm.to_markdown(pdf_file)
    
    return text
    


def section_spliiter(all_text: str = "") -> dict:
    pass