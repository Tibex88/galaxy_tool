import argparse
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = _parser().parse_args(argv)
    # print(args.d,args.str, args.file, args.bool)
    print("Query: ",type(args.query))
    print("Query: ",type(args.query[0]))
    print("Query: ",(args.query[0]))
    print("Query: ",(args.query))
    print("Prompt: ",args.prompt)
    exit_code = 0
    sys.exit(exit_code)

def _parser():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-d", type=str, help="directory target URI")
    # parser.add_argument("-str", type=str, help="file sources json")
    # parser.add_argument("-file", type=str, help="files to export")
    parser.add_argument("-prompt", type=str, help="NL prompt", default='No prompt')
    parser.add_argument("-query",nargs='+' , type=str, help="list of arguments", default='No query')
    # parser.add_argument("-select", type=str, help="select type")
    return parser


if __name__ == "__main__":
    main()