def word_count(content):
    content_list = content.split()
    return len(content_list)

def char_count(content):
    char_count = dict()

    for char in content:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
            continue

        char_count[char] += 1

    return char_count

def char_sort(char_dict):
    sorted_char_list = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    # Example result: [('z', 25), ('a', 20), ('x', 15), ...]

    return_value = []

    for char_obj in sorted_char_list:
        char = char_obj[0]
        count = char_obj[1]

        if not char.isalpha():
            continue

        return_value.append({"char": char, "num": count})

    return return_value
