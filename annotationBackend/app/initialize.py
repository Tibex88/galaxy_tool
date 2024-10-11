import os

from .services.schema_data import SchemaManager
from .services.cypher_generator import CypherQueryGenerator
from .services.metta_generator import MeTTa_Query_Generator

databases = {
    # "metta": MeTTa_Query_Generator("./metta_data"),
    "cypher": CypherQueryGenerator("./cypher_data")
    # Add other database instances here
}

schema_config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'schema_config.yaml')
biocypher_config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'biocypher_config.yaml')
schema_manager = SchemaManager(schema_config_path=schema_config_path , biocypher_config_path=biocypher_config_path)
