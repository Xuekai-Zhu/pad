def solution():
    # Set variables for the name Florence and the centaur named Firenze
    name_florence = "Florence"
    harry_potter_character = "Firenze"
    books_appeared_in = 3
    movies_appeared_in = 1
    # Check if Firenze is named after Florence
    if harry_potter_character.startswith(name_florence):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())