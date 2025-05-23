def sort_list(characters):
    sorted_list = []

    for i in characters:
        sorted_list.append({"char" : i, "num" : characters.get(i)})
    
    def sort_on(dict):
        return dict["num"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

charcters = {'a' : 4, 'c' : 10, 'b' : 7}

sort_list(charcters)