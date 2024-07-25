import argparse
import sys

class Node:
    def __init__(self, node_type, node_id, properties):
        self.type = node_type
        self.id = node_id
        self.properties = properties

    def __repr__(self):
        return f"Node(type={self.type}, id={self.id}, properties={self.properties})"

class Edge:
    def __init__(self, source, target, edge_type):
        self.source = source
        self.target = target
        self.type = edge_type

    def __repr__(self):
        return f"Edge(source={self.source}, target={self.target}, type={self.type})"


def parse_node(value):
    try:
        parts = value.split(',')
        if len(parts) < 3:
            raise ValueError("Insufficient parts for node")
        node_type = parts[0]
        node_id = parts[1]
        properties = parts[2:]
        return Node(node_type, node_id, properties)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid format for node: {value}. Expected format: type,id,property1,property2,...")

def parse_edge(value):
    try:
        parts = value.split(',')
        if len(parts) != 3:
            raise ValueError("Incorrect parts for edge")
        source = parts[0]
        target = parts[1]
        edge_type = parts[2]
        return Edge(source, target, edge_type)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid format for edge: {value}. Expected format: source,target,type")

class NodeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        nodes = [parse_node(value) for value in values]
        setattr(namespace, self.dest, nodes)

class EdgeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        edges = [parse_edge(value) for value in values]
        setattr(namespace, self.dest, edges)


def _parser():
    # Argument Parsing Setup
    parser = argparse.ArgumentParser(description="Process nodes and edges.")
    parser.add_argument('--nodes', nargs='+', action=NodeAction, help='List of nodes in the format type,id,property1,property2,...')
    parser.add_argument('--edges', nargs='+', action=EdgeAction, help='List of edges in the format source,target,type', default="No edges")

    return parser


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = _parser().parse_args(argv)
    # print("Nodes:", args.nodes)
    # print("Edges:", args.edges)

    print("Nodes: ",type(args.nodes))
    print("Edges: ",type(args.edges))
    # print("Nodes: ",(args.nodes))
    # print("Edges: ",(args.edges))
    exit_code = 0
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
