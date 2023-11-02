def solution():
    """Sally sews 4 shirts on Monday, 3 shirts on Tuesday, and 2 shirts on Wednesday. Each shirt has 5 buttons. How many buttons does Sally need to sew all the shirts?"""
    shirts_monday = 4
    shirts_tuesday = 3
    shirts_wednesday = 2
    total_shirts = shirts_monday + shirts_tuesday + shirts_wednesday
    buttons_per_shirt = 5
    total_buttons = total_shirts * buttons_per_shirt
    return total_buttons

print(solution())