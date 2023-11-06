from faker import Faker

import json

fake = Faker()

color_list = []



def create_list_of_colors(lst):
    """Create random list of colors using faker

    Args:
        lst: Any list you want to add colors too

    Returns:
        Random List of colors
    """
    for i in range(20):
        lst.append(fake.color_name())
    return lst


create_list_of_colors(color_list)



def remove_duplicates(lst):
    """Remove duplicates from a list

    Args:
        lst: Any list you want duplicates removed from

    Returns:
        set: returns a set with no duplicates
    """
    lst = str(set(lst))
    return lst

remove_duplicates(color_list)




len_list_color_list = []
for element in color_list:
        len_list_color_list.append(len(element))


color_dict = dict(zip(color_list, len_list_color_list))


with open("./color_dict.json", "w") as json_file:
    json.dump(color_dict, json_file)



with open("./color_dict.json", "r") as json_file:
    new_color_dict = json.load(json_file)




