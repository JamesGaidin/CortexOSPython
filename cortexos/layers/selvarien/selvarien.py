import json
import os

class Selvarien:
    def __init__(self, filepath="data/symbols.json"):
        self.symbols = {}
        self.filepath = filepath
        self.load_symbols()

    def define_symbol(self, name, meaning):
        self.symbols[name] = meaning
        self.save_symbols()

    def get_meaning(self, name):
        return self.symbols.get(name, "Unknown")

    def interpret(self, phrase):
        return {word: self.get_meaning(word) for word in phrase.split()}

    def save_symbols(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.symbols, f, indent=2)

    def load_symbols(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.symbols = json.load(f)
