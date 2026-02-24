from googletrans import Translator

def english_to_kannada(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='kn')
    return translated.text

print("=== English to Kannada Translator ===")
print("Type 'exit' to stop\n")

while True:
    user_input = input("Enter English text: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    result = english_to_kannada(user_input)
    print("Kannada:", result)
    print()