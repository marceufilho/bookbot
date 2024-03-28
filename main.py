import os 
PATH = os.curdir
book_path = os.path.join(PATH, "books/frankenstein.txt")

def sort_on(dict):
    return dict["reps"]

def transform_dict_to_list(dict):
    list_of_dicts =[]
    for key in dict:
        list_of_dicts.append({"char" : key ,"reps" :  dict[key]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


def count_words(str_text):
    words = str_text.split()
    return len(words)

def count_char(str_text):
    chars = [*str_text.lower()]
    count_char = {}
    
    for char in chars:
        if not char.isalpha():
            continue
        if char not in count_char:
            count_char[char] = 0
        count_char[char] += 1
    return count_char


def main():
    dict_char = {}
    list_of_dicts = []
    with open(book_path, "r") as book:
        book_content = book.read()
        book.close()
    book_length = count_words(book_content)
    dict_char = count_char(book_content)
    list_of_dicts = transform_dict_to_list(dict_char)
    print(f"{book_length} words found in the document \n")
    for dic in list_of_dicts:
        print(f"The '{dic['char']}' character was found {dic['reps']} times")

main()

# count_char("""HIS eBook is for the use of anyone anywhere at no cost and with
# almost no restrictions whatsoever.  You may copy it, give it away or
# re-use it under the terms of the Project Gutenberg License included
# with this eBook or online at www.gutenberg.net""")