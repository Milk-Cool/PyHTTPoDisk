from os.path import join, isdir
from os import listdir, remove
from json import dumps, loads
import argparse
import requests
import base64
from time import sleep

parser = argparse.ArgumentParser(description="Processes files on a certain disk.")
parser.add_argument("path", metavar="path", type=str, help="The path to the disk")

args = parser.parse_args()
PATH = args.path

def list_requests():
    files = listdir(join(PATH, "req"))
    return files

def parse_request(name):
    f = open(join(PATH, "req", name), "r")
    obj = loads(f.read())
    f.close()
    return obj

def make_request(obj):
    r = requests.request(obj["method"], obj["url"], data=base64.b64decode(obj["data"]), headers=obj["headers"])
    return r

def write_response(name, res: requests.Response):
    f = open(join(PATH, "res", name), "w")
    obj = {
        "status": res.status_code,
        "headers": dict(res.headers),
        "body": base64.b64encode(res.content).decode()
    }
    f.write(dumps(obj))
    f.close()

def delete_request(name):
    remove(join(PATH, "req", name))

def main():
    print("Hello! Insert the USB stick to write the responses to it!")
    while True:
        if isdir(join(PATH, "req")) and isdir(join(PATH, "res")):
            reqs = list_requests()
            print(f"Found {len(reqs)} requests.")
            for i in reqs:
                req = parse_request(i)
                print(f"> {req["method"]} {req["url"]}")
                res = make_request(req)
                print(f"< {res.status_code}")
                write_response(i, res)
                delete_request(i)
        else:
            print("No valid disk found.")
        sleep(0.5)

if __name__ == "__main__":
    main()