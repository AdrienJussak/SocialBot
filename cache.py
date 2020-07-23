import json
import os


class CacheManager:

    def __init__(self) -> None:
        self.filename = 'cache.json'

        self.data = {}

        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.data = json.load(f)

    def get_data(self, data_id: str) -> object:
        if data_id in self.data:
            return self.data[data_id]
        return {}

    def set_data(self, data_id: str, data: object):
        self.data[data_id] = data
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.data))
