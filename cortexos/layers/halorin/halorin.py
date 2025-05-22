class Halorin:
    def __init__(self, name="Velinari"):
        self.name = name

    def speak(self, message):
        """Outputs a message from the AI companion."""
        print(f"[{self.name}]: {message}")

    def ask(self, prompt):
        """Prompts the user and returns the input."""
        try:
            return input(f"{self.name} asks: {prompt}")
        except KeyboardInterrupt:
            print(f"\n[{self.name}]: Interrupted. Closing session.")
            exit()

    def react(self, message, emotion=None):
        """Optional emotional variation system (stub for future)"""
        if emotion == "happy":
            print(f"[{self.name} 🌞]: {message}")
        elif emotion == "sad":
            print(f"[{self.name} 🌧️]: {message}")
        else:
            self.speak(message)

    def confirm(self, question):
        """Asks for confirmation (yes/no)"""
        response = input(f"{self.name} asks (y/n): {question} ").strip().lower()
        return response in ["yes", "y"]

    def goodbye(self):
        self.speak("Memory stabilized. Halorin signing off for now.")
