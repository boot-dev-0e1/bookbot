import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import count_book_words, count_book_characters, sorted

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#def count_book_words(book_text):
#    return len(book_text.split())

def main():
    #book = 'books/frankenstein.txt'
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    text = get_book_text(book)
    print("----------- Word Count ----------")
    print(f"Found {count_book_words(text)} total words")
    print("--------- Character Count -------")
    #print(count_book_characters(text))
    sorted_char_count = sorted(count_book_characters(text))
    for char_dict in sorted_char_count:
        for key in char_dict.keys():
            print(key + ": " + str(char_dict[key]))
    print("============= END ===============")
main()
