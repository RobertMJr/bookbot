def count_words(text):
    word_count = text.split()
    num_words = len(word_count)
    return num_words

def count_chars(text):
    result = {}
    for char in text.lower():
        if char in result.keys():
            result[char] += 1
        else:
            result[char] = 1
    return result

# Helper function to allow sorting a list of dictionaries based on the 'num' key and its coresponding values in those dictionaries
def sort_on(items):
    return items["num"]

'''
Function that takes a dictionary of type: {'a': 3, 'd': 7, 'b': 2, 's': 9...etc}
Creates a list of dictionaries of type 
[
    {'char': 'a', 'num': 3},
    {'char': 'd', 'num': 7},
    {'char': 'b', 'num': 2},
    {'char': 's', 'num': 9},
    
]
Sorts the list of dictionaries based on the 'num' key with the help of the above helper function.
Returns the sorted list of dictionaries
'''
def sort_dict(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char":key, "num":value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
