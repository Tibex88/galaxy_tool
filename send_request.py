from annotationBackend.app.process_query import process_query
from chatBackend.natural_laguage_query import answer_question

def send_request(prompt, query):
    if prompt == "No Prompt" and query == "No query":
        raise ValueError('argument can not be empty')

    response = process_query(query) if query != "No query" else answer_question(prompt)
    return response