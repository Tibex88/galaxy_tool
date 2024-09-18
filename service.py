import argparse
import sys


sample_query = {
  "nodes": [
    {
      "id": "8cc0bd89-7f53-4e89-aab4-cbac132be68b",
      "type": "custom",
      "data": {
        "type": "pathway"
      },
      "position": {
        "x": 101.98156752467406,
        "y": -49.84697884443683
      },
      "width": 96,
      "height": 132,
      "selected": False,
      "positionAbsolute": {
        "x": 101.98156752467406,
        "y": -49.84697884443683
      },
      "dragging": False
    },
    {
      "id": "57a11576-247c-4aa0-9147-0c61a05b01a5",
      "type": "custom",
      "data": {
        "type": "gene"
      },
      "position": {
        "x": -221.82220711239705,
        "y": -49.60076902967583
      },
      "width": 96,
      "height": 132,
      "selected": False,
      "positionAbsolute": {
        "x": -221.82220711239705,
        "y": -49.60076902967583
      },
      "dragging": False
    },
    {
      "id": "745a72cb-6639-4473-8bb9-d70f2acca303",
      "type": "custom",
      "data": {
        "type": "promoter"
      },
      "position": {
        "x": -566.2411719483079,
        "y": -179.1683301043495
      },
      "width": 96,
      "height": 132,
      "selected": False,
      "positionAbsolute": {
        "x": -566.2411719483079,
        "y": -179.1683301043495
      },
      "dragging": False
    },
    {
      "id": "8dfe763f-f417-432b-b529-22cd56307d8c",
      "type": "custom",
      "data": {
        "type": "super_enhancer"
      },
      "position": {
        "x": -568.6443836145361,
        "y": 102.01636778395108
      },
      "width": 115,
      "height": 132,
      "selected": False,
      "positionAbsolute": {
        "x": -568.6443836145361,
        "y": 102.01636778395108
      },
      "dragging": False
    }
  ],
  "edges": [
    {
      "animated": True,
      "label": "relates",
      "markerEnd": {
        "type": "arrowclosed",
        "color": "black"
      },
      "style": {
        "width": 5,
        "borderWidth": 5,
        "height": 5,
        "strokeWidth": 2,
        "strokeDasharray": "5,5"
      },
      "id": "8ee4b556-1603-4b75-860a-5d99195937f6",
      "source": "57a11576-247c-4aa0-9147-0c61a05b01a5",
      "target": "8cc0bd89-7f53-4e89-aab4-cbac132be68b",
      "type": "custom",
      "data": {
        "edgeType": "genes_pathways",
        "options": [
          {
            "type": "gene to pathway association",
            "label": "genes_pathways",
            "source": "gene",
            "target": "pathway"
          }
        ]
      }
    },
    {
      "animated": True,
      "label": "relates",
      "markerEnd": {
        "type": "arrowclosed",
        "color": "black"
      },
      "style": {
        "width": 5,
        "borderWidth": 5,
        "height": 5,
        "strokeWidth": 2,
        "strokeDasharray": "5,5"
      },
      "id": "03c6d01f-24be-4022-98e6-ef4adbc1dd15",
      "source": "745a72cb-6639-4473-8bb9-d70f2acca303",
      "target": "57a11576-247c-4aa0-9147-0c61a05b01a5",
      "type": "custom",
      "data": {
        "edgeType": "promoter_gene",
        "options": [
          {
            "type": "promoter to gene association",
            "label": "promoter_gene",
            "source": "promoter",
            "target": "gene"
          }
        ]
      },
      "selected": False
    },
    {
      "animated": True,
      "label": "relates",
      "markerEnd": {
        "type": "arrowclosed",
        "color": "black"
      },
      "style": {
        "width": 5,
        "borderWidth": 5,
        "height": 5,
        "strokeWidth": 2,
        "strokeDasharray": "5,5"
      },
      "id": "8a3403bf-a90f-405f-ace1-15f3ec00b130",
      "source": "8dfe763f-f417-432b-b529-22cd56307d8c",
      "target": "57a11576-247c-4aa0-9147-0c61a05b01a5",
      "type": "custom",
      "data": {
        "edgeType": "super_enhancer_gene",
        "options": [
          {
            "type": "super enhancer to gene association",
            "label": "super_enhancer_gene",
            "source": "super_enhancer",
            "target": "gene"
          }
        ]
      }
    }
  ],
  "viewport": {
    "x": 842.6593217014231,
    "y": 329.7835117829392,
    "zoom": 0.9478893479335839
  }
}

def main(argv=None):
  if argv is None:
      argv = sys.argv[1:]
  args = _parser().parse_args(argv)


  if args.template is not None:
    # insert logic
    template = args.template[1]
    print(template)
    return 1
  elif args.prompt is not None:
  # insert logic
    prompt = args.prompt
    print(prompt)
    return 1
  elif args.json is not None:
  # insert logic
    json = args.json
    print(json)
    return 1
  else:
    print("No template or prompt provided")

    
  exit_code = 0
  sys.exit(exit_code)

def _parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-prompt", type=str, help="Natural Language prompt for the program", default=None)
    parser.add_argument("-template",nargs='+', type=str, help="Index for query templates", default=None)
    parser.add_argument("-json", type=str, help="Path to a JSON file containing the source data", default=None)    # parser.add_argument("-select", type=str, help="select type")
    
    return parser


if __name__ == "__main__":
    main()