# from llama_index.llms.ollama import Ollama
from together import Together
from dotenv import load_dotenv
import json
import os

load_dotenv()

# base_url = os.getenv('BASE_URL')

def generate_json_request(user_question):
    prompt = f'''
    You are given a natural language query and your task is to generate a corresponding JSON request format. Below is an example of the JSON request structure:
    {{
      "requests": {{
        "nodes": [
          {{
            "node_id": "n1",
            "id": "",
            "type": "gene",
            "properties": {{}}
          }},
          {{
            "node_id": "n2",
            "id": "",
            "type": "transcript",
            "properties": {{}}
          }},
          {{
            "node_id": "n3",
            "id": "",
            "type": "protein",
            "properties": {{
              "protein_name": "MKKS"
            }}
          }}
        ],
        "predicates": [
          {{
            "type": "transcribed to",
            "source": "n1",
            "target": "n2"
          }},
          {{
            "type": "translates to",
            "source": "n2",
            "target": "n3"
          }}
        ]
      }}
    }}

    The nodes key contains the nodes the request is about, and the predicates key contains the mapping of relationships between the nodes in the nodes key.

    Here is an example of a natural language query: "What are the proteins that gene ENSG00000133710 codes for?"

    Your task is to convert the given natural language query into the corresponding JSON request format. Ensure the JSON request accurately reflects the information provided in the query, including the appropriate node types and relationships between them.

    Example Output:

    {{
      "requests": {{
        "nodes": [
          {{
            "node_id": "n1",
            "id": "ENSG00000133710",
            "type": "gene",
            "properties": {{}}
          }},
          {{
            "node_id": "n2",
            "id": "",
            "type": "transcript",
            "properties": {{}}
          }},
          {{
            "node_id": "n3",
            "id": "",
            "type": "protein",
            "properties": {{
              "protein_name": ""
            }}
          }}
        ],
        "predicates": [
          {{
            "type": "transcribed to",
            "source": "n1",
            "target": "n2"
          }},
          {{
            "type": "translates to",
            "source": "n2",
            "target": "n3"
          }}
        ]
      }}
    }}

    Note: The JSON request and natural language query provided are just examples. Use the given structure and information as a guide to generate similar JSON requests for other natural language queries. Output only the json request.

    Below is the natural language query that you are going to generate the json format request for:

    {user_question}
    '''

    # llm = Ollama(model="llama3", request_timeout=120.0, base_url=base_url, json_mode=True)
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

    print(response)
    return json.loads(response)['requests']

