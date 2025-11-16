def get_num_words(text: str) -> int:
    return len(text.split())


def character_count(text: str) -> int:
    dict_count = {}
    transformed_text = text.lower().replace(" ", "").replace("\n", "")
    for char in transformed_text:
        if char.isalpha():
            dict_count[char] = dict_count.get(char, 0) + 1
    return dict_count


def sort_dict(count_dict: dict) -> list:
    output_list = [{'char': k, 'num': v} for k,v in count_dict.items()]
    output_list.sort(reverse=True, key=lambda x: x.get('num'))
    return output_list