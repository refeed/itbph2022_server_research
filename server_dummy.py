import json
import logging
import os
import pymongo

from flask import Flask, request

MONGO_CONN_STRING = os.getenv("MONGO_CONN_STRING")

app = Flask(__name__)
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers

mongo_client = pymongo.MongoClient(MONGO_CONN_STRING)
admin_db = mongo_client["admin"]
transactions_col = admin_db["transactions"]

# TODO: Change the server engine
# Dummy server


@app.post("/api/v1/transaction")
def receive_transaction():
    # Needed data:
    # - Plat nomor (AAA 1234 BBB) -> max(10 bytes)
    # - Datetime -> 8 bytes
    # - Jenis BBM -> enum (1 byte), worst case string (20 bytes) -> max(20 bytes)
    # - Jumlah -> 8 bytes
    # - NIK pembeli -> 16 bytes
    # - No SPBU -> 20 bytes
    # data = request.get_json()
    # TODO: Add data to mongoDB
    # 10 + 8 + 20 + 8 + 16 + 20 = 82 bytes
    try:
        transactions_col.insert_one(request.get_json())
    except Exception as e:
        app.logger.exception(e)
        return json.dumps(dict(status=500)), 500

    return json.dumps(dict(status=201)), 201
