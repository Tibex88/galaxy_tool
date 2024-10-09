from llama_index.llms.ollama import Ollama
from together import Together
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('BASE_URL')


def summarize_json_response(json_response):
    prompt = f'''
    You are given a json format information and your task is to summarize the information in the json yourself and return the summary. Below is the json format information:

    Below is the json format query that you are going to generate a summarization for:
    {json_response}
    '''
    # llm = Ollama(model="llama3", request_timeout=120.0, base_url=base_url)
    # response = llm.complete(prompt)

    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

    stream = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[{"role": "user", "content": prompt}],
      stream=True,
    )

    response = ''
    for chunk in stream:
      response += chunk.choices[0].delta.content or ""

    return response