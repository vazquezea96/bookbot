def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count
