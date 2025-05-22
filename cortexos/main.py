from layers.selvarien import Selvarien
from layers.eluren import Eluren
from layers.halorin import Halorin

def main():
    # Initialize components
    halorin = Halorin("Velinari")
    symbols = Selvarien()
    memory = Eluren()

    halorin.speak("Welcome, James. Ready to build the future?")

    while True:
        cmd = halorin.ask("What do you want to do? (define / recall / interpret / quit): ").strip().lower()

        if cmd == "define":
            word = halorin.ask("Enter symbol name: ")
            meaning = halorin.ask("What does it mean? ")
            symbols.define_symbol(word, meaning)
            memory.remember(f"Defined '{word}' as '{meaning}'")
            halorin.speak("Symbol stored.")

        elif cmd == "recall":
            query = halorin.ask("Search memory for: ")
            results = memory.recall(query)
            if results:
                halorin.speak("I remember:")
                for r in results:
                    print(f"- {r}")
            else:
                halorin.speak("Nothing found.")

        elif cmd == "interpret":
            phrase = halorin.ask("Enter a phrase to interpret: ")
            result = symbols.interpret(phrase)
            for word, meaning in result.items():
                print(f"{word} => {meaning}")

        elif cmd == "quit":
            halorin.speak("Session ended. Memory retained.")
            break

        else:
            halorin.speak("I didn't understand that. Try again.")

if __name__ == "__main__":
    main()
