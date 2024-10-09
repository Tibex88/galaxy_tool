from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from .utils.json_request_generator import use_outlines
from .utils.generate_json_request_prompt import generate_json_request
from .utils.summarize_response_prompt import summarize_json_response
from annotationBackend.app.routes import process_query

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# local_model_path = os.getenv('LOCAL_MODEL_PATH')
base_url = os.getenv('BASE_URL')



app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

def answer_question(prompt):

    json_request = generate_json_request(prompt)
    # Make the POST request to the /query endpoint
    annotation_response = process_query(json_request)
    summarized_response = summarize_json_response(annotation_response)

    return summarized_response


if __name__ == '__main__':
    app.run(debug=True, port=5001)
