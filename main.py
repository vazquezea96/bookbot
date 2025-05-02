def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def count_words(words):
    document = get_book_text(words)

    string = document.split()

    count = len(string)

    return f"{count} words found in the document."

def main():
    get_book_text("./books/frankenstein.txt")
    print(count_words("./books/frankenstein.txt"))


main()
