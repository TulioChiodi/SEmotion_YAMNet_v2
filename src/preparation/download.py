import requests
from tqdm import tqdm
from zipfile import ZipFile
import gdown
import os
from pathlib import Path

def setup_folders(ROOT_PATH):
    ROOT_PATH = Path(ROOT_PATH)
    os.makedirs(ROOT_PATH / 'data/processed')
    os.makedirs(ROOT_PATH / 'data/raw')

def download(url: str, fpath: str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(fpath, 'wb') as file, tqdm(
            desc=fpath,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


def unzip(fpath: str, dest_path: str):
    
    with ZipFile(fpath, 'r') as zipObj:
       # Extract all the contents of zip file in different directory
       zipObj.extractall(dest_path)
        
    os.remove(fpath)
    

def gdrive_download(file_code, output):
    url = 'https://drive.google.com/uc?id=' + file_code
    gdown.download(url, output, quiet=False)
    
    
def get_ravdess(url : str = 'https://zenodo.org/record/1188976/files/Audio_Speech_Actors_01-24.zip?download=1',
                fpath : str = 'data/raw/RAVDESS.zip',
                dest_path : str = 'data/raw/RAVDESS'):
    
    download(url,fpath)
    unzip(fpath, dest_path)
    
    
def get_tess(file_code : str = '1ghworzNe_iGozTQSAPFbmaapJmsMmndC',
             fpath: str = 'data/raw/TESS.zip',
             dest_path : str = 'data/raw/TESS'):
    
    gdrive_download(file_code, fpath)
    unzip(fpath, dest_path)
    

def get_demos(file_code : str = '1jjU6jvjU82UHZiHXjOZXoBlU1e88vE5t',
             fpath: str = 'data/raw/DEMoS.zip',
             dest_path : str = 'data/raw/DEMoS'):
    
    gdrive_download(file_code, fpath)
    unzip(fpath, dest_path)
    
    
def get_datasets():
    
    get_ravdess()
    get_tess()
    get_demos()


