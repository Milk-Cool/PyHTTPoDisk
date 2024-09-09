import json
import logging
from os.path import join, isfile
from os import remove
from mitmproxy import ctx
from mitmproxy import http
from time import sleep
import base64

n = 0

def load(loader):
    loader.add_option(
        name="disk",
        typespec=str,
        default="req",
        help="The location of the disk with requests",
    )

def request(flow: http.HTTPFlow):
    global n
    cn = n
    n += 1
    logging.info(f"{cn} > {flow.request.method} {flow.request.url}")
    freq = open(join(ctx.options.disk, "req", str(cn)), "w")
    freq.write(json.dumps({
        "method": flow.request.method,
        "url": flow.request.url,
        "data": base64.b64encode(flow.request.content).decode(),
        "headers": dict(flow.request.headers)
    }))
    freq.close()
    logging.info(f"{cn} ~ Waiting for response...")
    while not isfile(join(ctx.options.disk, "res", str(cn))):
        sleep(0.5)
    fres = open(join(ctx.options.disk, "res", str(cn)), "r")
    res = json.loads(fres.read())
    fres.close()
    remove(join(ctx.options.disk, "res", str(cn)))
    logging.info(f"{cn} < {res["status"]} {flow.request.url}")
    flow.response = http.Response.make(
        res["status"],
        base64.b64decode(res["body"]),
        res["headers"]
    )
    logging.info(f"{cn} ! Done!")
