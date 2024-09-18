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

query_templates = [
  {
    "id": "1",
    "title":
      "Find all GWAS variants of a gene that are located in enhancers and identify the associated genes of these enhancers",
    "query": {
      "nodes": [
        {
          "id": "f478dda6-bd11-4ce4-9188-a5c5a29dfeca",
          "type": "custom",
          "data": {
            "type": "snp",
          },
          "position": {
            "x": 35.859375,
            "y": 88.7578125,
          },
          "width": 96,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": 35.859375,
            "y": 88.7578125,
          },
          "dragging": False,
        },
        {
          "id": "2da4151b-9b1c-4c53-8aa5-05bdcfcccef1",
          "type": "custom",
          "data": {
            "type": "gene",
          },
          "position": {
            "x": 430.93955380234166,
            "y": -31.50848749276527,
          },
          "width": 96,
          "height": 132,
          "selected": True,
          "positionAbsolute": {
            "x": 430.93955380234166,
            "y": -31.50848749276527,
          },
          "dragging": False,
        },
        {
          "id": "3d4f0f03-8bf2-4f46-ba26-ceecfbe19542",
          "type": "custom",
          "data": {
            "type": "enhancer",
          },
          "position": {
            "x": 29.066685983068624,
            "y": -127.63988357649316,
          },
          "width": 96,
          "height": 132,
          "positionAbsolute": {
            "x": 29.066685983068624,
            "y": -127.63988357649316,
          },
        },
      ],
      "edges": [
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
          },
          "id": "e6f97dab-a52b-4fae-b87b-4b3d57fb0ac0",
          "source": "f478dda6-bd11-4ce4-9188-a5c5a29dfeca",
          "target": "2da4151b-9b1c-4c53-8aa5-05bdcfcccef1",
          "type": "custom",
          "data": {
            "edgeType": "in_gene",
            "options": [
              {
                "type": "gtex variant to gene expression association",
                "label": "gtex_variant_gene",
                "source": "snp",
                "target": "gene",
              },
              {
                "type": "upstream gene to variant association",
                "label": "upstream_gene",
                "source": "snp",
                "target": "gene",
              },
              {
                "type": "downstream gene to variant association",
                "label": "downstream_gene",
                "source": "snp",
                "target": "gene",
              },
              {
                "type": "in gene to variant association",
                "label": "in_gene",
                "source": "snp",
                "target": "gene",
              },
              {
                "type": "activity by contact",
                "label": "activity_by_contact",
                "source": "snp",
                "target": "gene",
              },
            ],
          },
        },
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
          },
          "id": "3714e51c-67be-489c-9290-a674fdf79daf",
          "source": "3d4f0f03-8bf2-4f46-ba26-ceecfbe19542",
          "target": "2da4151b-9b1c-4c53-8aa5-05bdcfcccef1",
          "type": "custom",
          "data": {
            "edgeType": "enhancer_gene",
            "options": [
              {
                "type": "enhancer to gene association",
                "label": "enhancer_gene",
                "source": "enhancer",
                "target": "gene",
              },
            ],
          },
        },
      ],
      "viewport": {
        "x": 238.4120676317035,
        "y": 286.81884278406613,
        "zoom": 0.2,
      },
    },
  },
  {
    "id": "2",
    "title":
      "For a set of co-expressed genes, what transcription factors appear to be controlling their coordinated expression?",
    "query": {
      "nodes": [
        {
          "id": "80952f5c-cb5b-4c01-9e8d-96c373459168",
          "type": "custom",
          "data": {
            "type": "gene",
          },
          "position": {
            "x": -8.853459278134608,
            "y": -29.236070695359416,
          },
          "width": 96,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": -8.853459278134608,
            "y": -29.236070695359416,
          },
          "dragging": False,
        },
        {
          "id": "fe0dbb9b-686e-4a60-aefb-e02daf201d43",
          "type": "custom",
          "data": {
            "type": "gene",
          },
          "position": {
            "x": 384.4859189688678,
            "y": 134.2244329525066,
          },
          "width": 96,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": 384.4859189688678,
            "y": 134.2244329525066,
          },
          "dragging": False,
        },
        {
          "id": "0471c125-a3fe-44f4-9bd5-7ed9ce9fd536",
          "type": "custom",
          "data": {
            "type": "transcript",
          },
          "position": {
            "x": 645.1978733983276,
            "y": -175.43152507915806,
          },
          "width": 96,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": 645.1978733983276,
            "y": -175.43152507915806,
          },
          "dragging": False,
        },
      ],
      "edges": [
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
          },
          "id": "f4c1bdec-b195-4094-812b-50410a624270",
          "source": "80952f5c-cb5b-4c01-9e8d-96c373459168",
          "target": "fe0dbb9b-686e-4a60-aefb-e02daf201d43",
          "type": "custom",
          "data": {
            "edgeType": "coexpressed_with",
            "options": [
              {
                "type": "gene to gene coexpression association",
                "label": "coexpressed_with",
                "source": "gene",
                "target": "gene",
              },
              {
                "type": "transcription factor to gene association",
                "label": "tf_gene",
                "source": "gene",
                "target": "gene",
              },
            ],
          },
        },
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
          },
          "id": "37e0103c-8024-455c-a3e8-474db91cb736",
          "source": "80952f5c-cb5b-4c01-9e8d-96c373459168",
          "target": "0471c125-a3fe-44f4-9bd5-7ed9ce9fd536",
          "type": "custom",
          "data": {
            "edgeType": "transcribed_to",
            "options": [
              {
                "type": "transcribed to",
                "label": "transcribed_to",
                "source": "gene",
                "target": "transcript",
              },
            ],
          },
        },
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
          },
          "source": "fe0dbb9b-686e-4a60-aefb-e02daf201d43",
          "sourceHandle": None,
          "target": "0471c125-a3fe-44f4-9bd5-7ed9ce9fd536",
          "targetHandle": None,
          "type": "custom",
          "data": {
            "options": [
              {
                "type": "transcribed to",
                "label": "transcribed_to",
                "source": "gene",
                "target": "transcript",
              },
            ],
          },
          "id": "reactflow__edge-fe0dbb9b-686e-4a60-aefb-e02daf201d43-0471c125-a3fe-44f4-9bd5-7ed9ce9fd536",
        },
      ],
      "viewport": {
        "x": 237.3047112650321,
        "y": 304.9378633544265,
        "zoom": 1.1234686581673015,
      },
    },
  },
  {
    "id": "3",
    "title":
      "Find all promoters and super enhancers associated with genes in a particular biological pathway",
    "query": {
      "nodes": [
        {
          "id": "8cc0bd89-7f53-4e89-aab4-cbac132be68b",
          "type": "custom",
          "data": {
            "type": "pathway",
          },
          "position": {
            "x": 101.98156752467406,
            "y": -49.84697884443683,
          },
          "width": 96,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": 101.98156752467406,
            "y": -49.84697884443683,
          },
          "dragging": False,
        },
        {
          "id": "57a11576-247c-4aa0-9147-0c61a05b01a5",
          "type": "custom",
          "data": {
            "type": "gene",
          },
          "position": {
            "x": -221.82220711239705,
            "y": -49.60076902967583,
          },
          "width": 96,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": -221.82220711239705,
            "y": -49.60076902967583,
          },
          "dragging": False,
        },
        {
          "id": "745a72cb-6639-4473-8bb9-d70f2acca303",
          "type": "custom",
          "data": {
            "type": "promoter",
          },
          "position": {
            "x": -566.2411719483079,
            "y": -179.1683301043495,
          },
          "width": 96,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": -566.2411719483079,
            "y": -179.1683301043495,
          },
          "dragging": False,
        },
        {
          "id": "8dfe763f-f417-432b-b529-22cd56307d8c",
          "type": "custom",
          "data": {
            "type": "super_enhancer",
          },
          "position": {
            "x": -568.6443836145361,
            "y": 102.01636778395108,
          },
          "width": 115,
          "height": 132,
          "selected": False,
          "positionAbsolute": {
            "x": -568.6443836145361,
            "y": 102.01636778395108,
          },
          "dragging": False,
        },
      ],
      "edges": [
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
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
                "target": "pathway",
              },
            ],
          },
        },
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
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
                "target": "gene",
              },
            ],
          },
          "selected": False,
        },
        {
          "animated": True,
          "label": "relates",
          "markerEnd": {
            "type": "arrowclosed",
            "color": "black",
          },
          "style": {
            "width": 5,
            "borderWidth": 5,
            "height": 5,
            "strokeWidth": 2,
            "strokeDasharray": "5,5",
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
                "target": "gene",
              },
            ],
          },
        },
      ],
      "viewport": {
        "x": 842.6593217014231,
        "y": 329.7835117829392,
        "zoom": 0.9478893479335839,
      },
    },
  },
]

def main(argv=None):
  if argv is None:
      argv = sys.argv[1:]
  args = _parser().parse_args(argv)


  if args.template is not None:
    # insert logic
    template = args.template[1]
    # print(query_templates[int(template)]["query"])
    print(sample_query)

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