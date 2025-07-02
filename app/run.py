import os

os.system("uvicorn app.main:app --ssl-keyfile=key.pem --ssl-certfile=cert.pem --reload")
