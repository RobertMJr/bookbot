import sys
from stats import count_words, count_chars, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def sorting_key(items):
    return items["num"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    output = get_book_text(sys.argv[1])
    word_count = count_words(output)
    char_count = count_chars(output)
    sorted_dicts = sort_dict(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_dicts:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")


main()