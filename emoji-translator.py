import json

emoji_mappings = {
    "happy": "😊",
    "love": "❤️",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "rain": "🌧️",
    "pizza": "🍕",
    "coffee": "☕",
    "sad": "😢",
    "cool": "😎",
    "fire": "🔥",
}

SAVE_FILE = "emoji_translator.json"

def translate_sentences(sentence, mapping):
    for word, emoji in mapping.items():
        sentence = sentence.replace(word, emoji)
    return sentence

def save_translation(sentence):
    with open(SAVE_FILE, "a") as file:
        file.write(sentence + "\n")
    print(f"Translated sentence saved to: {SAVE_FILE}")

def update_mapping(mappings):
    keyword = input("Enter the keyword: ").strip().lower()
    emoji = input(f"Enter the emoji for '{keyword}': ").strip() #chekc kr
    mappings[keyword] = emoji
    print(f"Updated mappings: {keyword} -> {emoji}")

def preview_emojis(mappings):
    print("\nSupported Emojis: ")
    for keyword, emoji in mappings.items():
        print(f"{keyword} -> {emoji}")
    print()



def main():
    print("\nWelcome to Emoji Translator!")
    while True:
        print("\nOptions: ")
        print("1. Translate a sentence")
        print("2. Add an emoji mapping")
        print("3. Preview supported emojis")
        print("4. Exit")
        choice = input("Choose the options(1-4): ").strip()

        if choice == '1':
            sentence = input("Enter a sentence to translate: ").strip().lower()
            translated_sentence = translate_sentences(sentence, emoji_mappings)

            print(f"Translated sentence is: {translated_sentence}")
            save_option = input("Save this translation? (yes/no): ").strip().lower()

            if save_option == "yes":
                save_translation(translated_sentence)

        elif choice == '2':
            update_mapping(emoji_mappings)

        elif choice == '3':
            preview_emojis(emoji_mappings)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()