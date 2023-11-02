def solution():
    """Pauline has a garden with vegetables. In it, Pauline has planted 3 kinds of tomatoes - 5 of each kind, 5 kinds of cucumbers - 4 of each kind, and 30 potatoes. In the whole garden, there are 10 rows with 15 spaces in each to plant any vegetable. How many more vegetables could Pauline plant in her garden?"""
    # Define the number of vegetables currently in the garden
    tomatoes = 15  # 3 kinds of tomatoes with 5 each
    cucumbers = 20  # 5 kinds of cucumbers with 4 each
    potatoes = 30

    # Calculate the total number of spaces in the garden
    total_spaces = 10 * 15

    # Calculate the number of spaces used
    used_spaces = tomatoes + cucumbers + potatoes

    # Calculate the number of spaces available
    available_spaces = total_spaces - used_spaces

    # return the result
    result = available_spaces
    return result

print(solution())