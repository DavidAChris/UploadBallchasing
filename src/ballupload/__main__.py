import os
from UploadApi import upload_handler
os.environ['CONFIGS'] = '../../configuration/Configs.yaml'

if __name__ == '__main__':
    upload_handler()
