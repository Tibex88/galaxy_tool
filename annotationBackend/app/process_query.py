import logging
import json
import yaml
import os
from .initialize import databases, schema_manager
from .lib.validator import validate_request
# Setup basic logging
logging.basicConfig(level=logging.DEBUG)

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logging.info("Configuration loaded successfully.")
        return config
    except FileNotFoundError:
        logging.error(f"Config file not found at: {config_path}")
        raise
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML file: {e}")
        raise

config = load_config()

def process_query(query):

    node_map = validate_request(query, schema_manager.schema)
    if node_map is None:
        raise ValueError("invalid node_map returned by validate request")

    database_type = config['database']['type']
    db_instance = databases[database_type]
    # Generate the query code
    query_code = db_instance.query_Generator(query, node_map)
    
    # Run the query and parse the results
    result = db_instance.run_query(query_code)
    parsed_result = db_instance.parse_and_serialize(result, schema_manager.schema)
    
    response_data = {
        "nodes": parsed_result[0],
        "edges": parsed_result[1]
    }
    
    formatted_response = json.dumps(response_data, indent=4)
    return formatted_response


