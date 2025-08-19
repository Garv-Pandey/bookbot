from stats import word_count

def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print ("main")
    contents = get_book_text("./books/frankenstein.txt") 
    num_words = word_count(contents)
    print(f'{num_words} words found in the document')

    return 0

main()
