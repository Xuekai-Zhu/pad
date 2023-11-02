def solution():
    """A curry house sells curries that have varying levels of spice. Recently, a lot of the customers have been ordering very mild curries and the chefs have been having to throw away some wasted ingredients. To reduce cost and food wastage, the curry house starts monitoring how many ingredients are actually being used and changes their spending accordingly. The curry house needs 3 peppers for very spicy curries, 2 peppers for spicy curries, and only 1 pepper for mild curries. After adjusting their purchasing, the curry house now buys the exact amount of peppers they need. Previously, the curry house was buying enough peppers for 30 very spicy curries, 30 spicy curries, and 10 mild curries. They now buy enough peppers for 15 spicy curries and 90 mild curries. They no longer sell very spicy curries. How many fewer peppers does the curry house now buy?"""
    # Calculate the total number of peppers needed previously
    previous_peppers = (30*3) + (30*2) + (10*1)

    # Calculate the total number of peppers needed now
    now_peppers = (15*2) + (90*1)

    # Calculate the difference in the number of peppers
    pepper_difference = previous_peppers - now_peppers

    result = pepper_difference
    return result

print(solution())