
print("PERSONAL AI TUTOR")
print("Type 'exit' to stop chatting.")

while True:
    question = input("\nYou: ").lower()

    if question == "exit":
        print("Tutor: Goodbye! Keep learning.")
        break

    elif "hello" in question or "hi" in question:
        print("Tutor: Hello! What would you like to learn today?")

    elif "newton" in question:
        print("Tutor: Newton's laws explain how objects move.")
        print("There are three laws of motion.")

    elif "work" in question:
        print("Tutor: In Physics, work is done when a force")
        print("causes displacement in an object.")

    elif "energy" in question:
        print("Tutor: Energy is the capacity to do work.")

    elif "python" in question:
        print("Tutor: Python is a programming language")
        print("used to build software and AI applications.")

    else:
        print("Tutor: I don't know that topic yet.")
        print("I'll learn to handle more questions as we develop me.")