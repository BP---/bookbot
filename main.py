def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))
    print(count_letters(file_contents))
    print_report(count_words(file_contents), count_letters(file_contents))

def count_words(text):
    
    words = text.split()
    word_count = len(words)

    return word_count

def count_letters(text):
    
    words = text.split()
    letters = {}
    for word in words:
        for letter in word:
            if letter.lower() in letters:
                letters[letter.lower()] += 1
            else:
                letters[letter.lower()] = 1


    return letters

def print_report(word_count, letter_count):
    print(f"Total words: {word_count}")
    char_list = list(letter_count)
    alphabet_list = []
    for char in char_list:
        if char.isalpha():
            alphabet_list.append(char)
    alphabet_list.sort()
    for char in alphabet_list:
        print(f"{char} was found {letter_count[char]} times")
    print("---End report---")
    


if __name__ == "__main__":
    main()