# post_test_data_ingestion_day_1
1. Buat virtual Environment
  ```
  python3 -m venv .venv
  source .venv/bin/activate
  ```
2. Install dependencies:
   ```
     pip install -r requirements.txt
   ```  
3. Buat file .env masukan sesuai dengan SFTP_HOST, SFTP_PORT, SFTP_USER, SFTP_PASSWORD yang dimiliki.
   ```
   SFTP_HOST={YOUR_SFTP_HOST}
   SFTP_PORT={YOUR_SFTP_PORT}
   SFTP_USER={YOUR_SFTP_USER}
   SFTP_PASSWORD={YOUR_SFTP_PASSWORD}
   ```
5. run extract.py
   ```
     python3 extract.py
   ```  
6. run transform.py
   ```
     python3 transform.py
   ```
7. run load.py
   ```
     python3 load.py
   ```  
