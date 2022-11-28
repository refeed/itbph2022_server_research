import json
import os
import pymongo

from flask import Flask, request

MONGO_CONN_STRING = os.getenv("MONGO_CONN_STRING")

app = Flask(__name__)

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
    # - Jenis BBM -> enum (1 byte), worst case string (50 bytes) -> max(50 bytes)
    # - Jumlah -> 64 bytes
    # - NIK pembeli ->
    # - No SPBU ->
    # data = request.get_json()
    # TODO: Add data to mongoDB
    # app.logger.warning("test")
    try:
        transactions_col.insert_one(request.get_json())
    except Exception:
        return json.dumps(dict(status=500)), 500

    return json.dumps(dict(status=201)), 201
