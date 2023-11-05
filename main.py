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
# print(create_list_of_colors(color_list))

create_list_of_colors(color_list)

# print(color_list)

def remove_duplicates(lst):
    """Remove duplicates from a list

    Args:
        lst: Any list you want duplicates removed from

    Returns:
        set: returns a set with no duplicates
    """
    lst = str(set(lst))
    return lst
# print(remove_duplicates(color_list))
remove_duplicates(color_list)

# print(color_list)


# print(remove_duplicates(color_list))

for element in color_list:
    color_dict = dict.fromkeys(color_list, len(element))
    print(len(element))
# Bug in this for loop. The print statement on line 34 produces the desired output. But using the same len(element) on line 33 does not give me the desired result in the color_dict variable.
print(color_dict)




with open("./color_dict.json", "w") as json_file:
    json.dump(color_dict, json_file)

print("json done")

with open("./color_dict.json", "r") as json_file:
    new_color_dict = json.load(json_file)

print(new_color_dict)


