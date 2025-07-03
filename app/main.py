import cohere
import argparse
import summarizer
import utils
from dotenv import load_dotenv
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf_file', help='PDF document containing the research paper', default="")
    parser.add_argument('--prompt', help='A specific prompt to ask about the paper', default="")

    args = parser.parse_args()

    load_dotenv()

    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    
    co = cohere.ClientV2(
        COHERE_API_KEY
    )

    doc_text = utils.pdf_to_text(pdf_file=args.pdf_file)
    
    response = summarizer.summarize_all(user_message=args.prompt, doc_text=doc_text, co=co)

    print(response.message.content[0].text)


if __name__ == "__main__":
    main()