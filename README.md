Use Python's Faker library to generate a list of twenty colors. Call it color_list.
This is just like using fake.name() in previous episodes, but use fake.color_name() instead. For details, read the Faker docs.
Remember to put Faker in your `requirements.txt`, and to install it.
Also remember to import it at the top of your code.

Write a function to remove any duplicates from color_list.
Once color_list only has unique values (no duplicates), write a function that creates a dictionary from it. Each value in the dictionary should be the name of the color, and its key should be the length of the name. Call it color_dict.
For instance, the list ["pink"] would create the dictionary {"pink": 4}, because the word "pink" has four letters.

Write color_dict into a JSON file. Include this file in your GitHub repository.


Read the color_dict back out of the JSON file and into a Python dictionary.
