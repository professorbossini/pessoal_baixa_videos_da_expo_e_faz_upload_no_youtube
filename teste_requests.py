import requests
import shutil

def download_file(url):
    local_filename = url.split('=')[-1] + '.mp4'
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename
download_file ('https://drive.google.com/uc?id=1mBW4vZ4yteyd6_m3yCRyrvGcUbw-WGeo')