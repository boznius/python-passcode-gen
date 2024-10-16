# Script to generate iPhone passcode from words or characters

def word_to_passcode(word):
    # Phone keypad mapping
    keypad = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
        '0': '0', '1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6', '7': '7',
        '8': '8', '9': '9'
    }

    # Convert the word to uppercase and remove any non-alphanumeric characters
    cleaned_word = ''.join(filter(str.isalnum, word.upper()))

    passcode = ''
    for char in cleaned_word:
        if char in keypad:
            passcode += keypad[char]
        else:
            # If character is not in keypad mapping, skip it
            pass

    # Limit the passcode to 6 digits (common iPhone passcode length)
    return passcode[:6]

# Example usage
if __name__ == "__main__":
    input_word = input("Enter a word or characters to generate passcode: ")
    generated_passcode = word_to_passcode(input_word)
    print(f"Generated iPhone passcode: {generated_passcode}")

