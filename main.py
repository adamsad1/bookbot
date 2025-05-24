from stats import *
import sys

def get_book_text(file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()

    return file_contents

def main():
    try:
        file_path = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_contents = get_book_text(file_path)
    file_length = get_num_words(file_contents)
    letter_count = get_unique_letters(file_contents)
    sorted_list = sort_list(letter_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at ", file_path)
    print("----------- Word Count ----------")
    print(f'Found {file_length} total words')
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha() == True:
            print(i["char"], ": ", i["num"], sep='')
    print("============= END ===============")
    #print(letter_count)

main()