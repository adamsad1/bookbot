def get_num_words(file_contents):
    return len(file_contents.split())

def get_unique_letters(file_contents):
    unique_words = {}
    file_content_list = file_contents.lower()
    
    for i in file_content_list:
        if i in unique_words:
            unique_words[i] = unique_words.get(i) + 1
        else:
            unique_words[i] = unique_words.get(i, 1)

    return unique_words

def sort_list(characters):
    sorted_list = []

    return sorted_list

def sort_list(characters):
    sorted_list = []

    for i in characters:
        sorted_list.append({"char" : i, "num" : characters.get(i)})
    
    def sort_on(dict):
        return dict["num"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
