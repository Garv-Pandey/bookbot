def get_book_text(file_path):
    file_contents = None
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print ("main")
    contents = get_book_text("./books/frankenstein.txt") 
    print(contents)

    return 0

main()
