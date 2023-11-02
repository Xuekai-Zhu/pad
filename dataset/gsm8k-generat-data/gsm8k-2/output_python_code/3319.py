def solution():
    """Pauline has a garden with vegetables. In it, Pauline has planted 3 kinds of tomatoes - 5 of each kind, 5 kinds of cucumbers - 4 of each kind, and 30 potatoes. In the whole garden, there are 10 rows with 15 spaces in each to plant any vegetable. How many more vegetables could Pauline plant in her garden?"""
    tomatoes_planted = 3 * 5
    cucumbers_planted = 5 * 4
    potatoes_planted = 30
    total_planted = tomatoes_planted + cucumbers_planted + potatoes_planted
    total_spaces = 10 * 15
    remaining_spaces = total_spaces - total_planted
    result = remaining_spaces
    return result

print(solution())