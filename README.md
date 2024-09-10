# PyHTTPoDisk
Make HTTP requests with a network-enabled and a non-network-enabled computer using a USB flash drive!

## Dependencies installation
```bash
python3 -m pip install -r requirements.txt
```
or, on Windows:
```bat
python -m pip install -r requirements.txt
```

## Running
1. Format a removable drive to FAT32 for maximum compatibility.
2. On the computer with internet, run:
```bash
python3 processor.py /media/user/FILES
```
or, on Windows:
```bat
python processor.py D:
```
where `/media/user/FILES` or `D:` is the drive mounting point.

3. On the computer without internet, insert the removable drive and run:
```bash
python3 client.py /media/user/FILES
```
or, on Windows:
```bat
python client.py D:
```
where `/media/user/FILES` or `D:` is the drive mounting point.

4. An HTTP proxy will be started on the device without internet access. Connect to it using the address `localhost:8080` (or host `localhost` and port `8080`).
5. Make a request, open a website, whatever.
6. Remove the removable drive and insert it into the computer with internet and the program running.
7. Wait for it to complete all requests.
8. Insert the drive into the computer without itnernet access.
9. All requests should now return a response.