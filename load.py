import pysftp
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_PORT = int(os.getenv("SFTP_PORT"))
SFTP_USER = os.getenv("SFTP_USER")
SFTP_PASS = os.getenv("SFTP_PASS")
REMOTE_FILE_PATH = os.getenv("REMOTE_FILE_PATH")
LOCAL_UPLOAD_FILE = os.getenv("LOCAL_UPLOAD_FILE")

def download_from_sftp():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    print(f"\nAttempting to connect to {SFTP_HOST} to download")
    try:
        with pysftp.Connection(
            host=SFTP_HOST,
            port=SFTP_PORT,
            username=SFTP_USER,
            password=SFTP_PASS,
            cnopts=cnopts,
        ) as sftp:
            print("Connection to SFTP server successful!")
            # upload file to sftp server
            print(f"Uploading '{LOCAL_UPLOAD_FILE}' tp '{REMOTE_FILE_PATH}'")
            sftp.put(LOCAL_UPLOAD_FILE, REMOTE_FILE_PATH)
            print("File uploaded successfully!")
    except Exception as e:
        print(f"An unexpected error occured during download: {e}")


download_from_sftp()