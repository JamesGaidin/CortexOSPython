import json
import os

class Eluren:
    def __init__(self, filepath="data/memory.json"):
        self.memory = []
        self.filepath = filepath
        self.load_memory()

    def remember(self, entry):
        self.memory.append(entry)
        self.save_memory()

    def recall(self, query):
        return [m for m in self.memory if query in m]

    def summarize(self):
        return self.memory[-5:]

    def save_memory(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=2)

    def load_memory(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.memory = json.load(f)
