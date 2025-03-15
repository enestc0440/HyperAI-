import hashlib
from datetime import datetime

class HyperNetwork:
    def __init__(self):
        self.nodes = {}
        self.blockchain = []

    def add_node(self, node_id):
        self.nodes[node_id] = {"data": {}, "timestamp": str(datetime.now())}

    def secure_upload(self, node_id, key, value):
        hashed_key = hashlib.sha256(key.encode()).hexdigest()
        self.nodes[node_id]["data"][hashed_key] = {
            "value": value,
            "signature": hashlib.sha256(str(value).encode()).hexdigest()
        }
        self._add_to_blockchain(f"{node_id}-{key}")

    def _add_to_blockchain(self, transaction):
        block = {
            "transaction": transaction,
            "timestamp": str(datetime.now()),
            "previous_hash": self.blockchain[-1]["hash"] if self.blockchain else "0"
        }
        block["hash"] = hashlib.sha256(str(block).encode()).hexdigest()
        self.blockchain.append(block)
