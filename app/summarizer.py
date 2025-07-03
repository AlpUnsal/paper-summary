from cohere import ClientV2

def summarize_all(user_message: str = "", doc_text: str = None, co:ClientV2 = None):
    if user_message == "":
        user_message = "Summarize this research paper by giving me 1. the core ideas" \
        " and 2. the findings and results." \
        " Ensure your answer is concise and cuts out anything unnecessary for literature review."

    res = co.chat(
        model="command-r7b-12-2024",
        messages=[
        {
            "role": "user",
            "content": user_message + "\n# PAPER\n" + doc_text,
        }
    ],
    )
    return res

def summarize_section(section_text:str = None, co:ClientV2 = None):
    pass

def create_insights(summarized_text):
    pass