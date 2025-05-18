def get_book_text(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()

    return file_contents

def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    file_length = len(file_contents.split())
    print(f'{file_length} words found in the document')

main()