def main():
    book_path  = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    count_of_characters = character_count(text)
    print(" --- Begin report of books/frankenstein.txt --- ")
    print(f"Number of words in the text is {word_count}")
    print("")
    printing_character_dictoinary(count_of_characters)
    print(" --- End Report --- ")
def get_book_text(path):
    with open(path)as f:
        return f.read()

def count_words(text):
    return len(text.split())

def character_count(text):
    characters = {}
    text = text.lower()
    for character in text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
            
    return characters

def printing_character_dictoinary(characters):
    char_count_list = []
    for key,value in characters.items():
        if key.isalpha():
            char_count_list.append({"name":key,"count":value})

    char_count_list.sort(reverse=True,key=sort_on)

    for dict in char_count_list:
        print(f"THe '{dict["name"]}' character was found {dict["count"]} times")

def sort_on(dict):
    return dict["count"]


main()
