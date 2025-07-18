from stats import get_num_words, get_character_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document.")
    char_count = get_character_count(text)
    print(f"{char_count}")


def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()



main()
