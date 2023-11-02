def solution():
    """A baker has 10 cheesecakes on the display while 15 more are still in the fridge. If the baker has sold 7 cheesecakes from the display, how many more cheesecakes are left to be sold?"""
    display_cheesecakes = 10
    fridge_cheesecakes = 15
    sold_cheesecakes = 7
    remaining_cheesecakes = display_cheesecakes + fridge_cheesecakes - sold_cheesecakes
    result = remaining_cheesecakes
    return result

print(solution())