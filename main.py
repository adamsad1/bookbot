from stats import get_num_words

def get_book_text(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()

    return file_contents

def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    file_length = get_num_words(file_contents)
    print(f'{file_length} words found in the document')

main()