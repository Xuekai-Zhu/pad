def solution():
    """Jack sews 3 shirts for each of his 3 kids. He sews 7 buttons in each shirt. How many buttons must Jack use for all the shirts?"""
    shirts_per_kid = 3
    num_kids = 3
    buttons_per_shirt = 7
    total_buttons = shirts_per_kid * num_kids * buttons_per_shirt
    result = total_buttons
    return result

print(solution())