import json
import sys

from flask import Flask, request

app = Flask(__name__)

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
    return json.dumps(dict(status=200)), 200
