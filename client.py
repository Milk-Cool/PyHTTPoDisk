from mitmproxy.tools.main import mitmdump
import argparse

parser = argparse.ArgumentParser(description="Writes requests to disk and waits for response.")
parser.add_argument("path", metavar="path", type=str, help="The path to the disk")

args = parser.parse_args()
PATH = args.path

mitmdump(args=["-s", "mitmmodule.py", "--set", "disk=" + PATH])