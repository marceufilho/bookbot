import os 

PATH = os.curdir
book_path = os.path.join(PATH, "books/frankenstein.txt")

def count_words(str_text):
    words = str_text.split()
    return len(words)

def count_char(str_text):
    chars = [*str_text.lower()]
    count_char = {}
    for char in chars:
        if char not in count_char:
            count_char[char] = 0
        count_char[char] += 1
    return count_char


def main():
    with open(book_path, "r") as book:
        book_content = book.read()
        book.close()
    book_length = count_words(book_content)
    print(book_length)
    print(count_char(book_content))

main()

# count_char("""HIS eBook is for the use of anyone anywhere at no cost and with
# almost no restrictions whatsoever.  You may copy it, give it away or
# re-use it under the terms of the Project Gutenberg License included
# with this eBook or online at www.gutenberg.net""")