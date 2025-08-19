import sys
from stats import word_count
from stats import char_count
from stats import char_sort

def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    print("============ BOOKBOT ============")

    book_address = sys.argv[1]
    print (f"Analyzing book found at {book_address}")


    contents = get_book_text(f"./{book_address}") 

    print("----------- Word Count ----------")
    num_words = word_count(contents)
    print(f'Found {num_words} total words')


    print("----------- Character Count----------")
    data = char_sort(char_count(contents))

    for d in data:
        print(f'{d["char"]}: {d["num"]}')

    return 0

main()
