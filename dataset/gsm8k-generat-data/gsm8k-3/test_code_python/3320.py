def solution():
    """Pauline has a garden with vegetables. In it, Pauline has planted 3 kinds of tomatoes - 5 of each kind, 5 kinds of cucumbers - 4 of each kind, and 30 potatoes. In the whole garden, there are 10 rows with 15 spaces in each to plant any vegetable. How many more vegetables could Pauline plant in her garden?"""
    # Calculate the number of tomatoes already planted
    tomatoes_planted = 3 * 5

    # Calculate the number of cucumbers already planted
    cucumbers_planted = 5 * 4

    # Calculate the total number of vegetables already planted
    vegetables_planted = tomatoes_planted + cucumbers_planted + 30

    # Calculate the total number of spaces in the garden
    total_spaces = 10 * 15

    # Calculate the number of vegetables that can still be planted
    vegetables_remaining = total_spaces - vegetables_planted

    # Display the number of vegetables that can still be planted
    result = vegetables_remaining
    return result

print(solution())