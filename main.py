def wc(book):
    words = book.split()
    return len(words)


def char_count(book):
    char_dict = dict()
    for ch in book.lower():
        if ch not in char_dict:
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1
    return char_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

        word_count = wc(file_contents)
        character_count = char_count(file_contents)

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()

        for k in character_count:
            if k.isalpha():
                print(f"The '{k}' character was found {character_count[k]} times")

        print("--- End report ---")


main()
