def count_book_words(book_text):
    return len(book_text.split())

def count_book_characters(book_text):
    characters = {}
    for char in book_text.lower():
        if char not in characters.keys():
            characters[char] = 1
        else:
            characters[char] +=1
    return characters

def sorted_on(dict):
    return(dict.keys())

def sorted(character_dict):
    alpha_dict = {key:value for key,value in character_dict.items() if key.isalpha()}
    alpha_list = [{key:alpha_dict[key]} for key,value in alpha_dict.items()]
    alpha_list.sort(reverse=True, key=sorted_on)
    return alpha_list

