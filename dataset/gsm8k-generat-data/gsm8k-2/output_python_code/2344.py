def solution():
    """A curry house sells curries that have varying levels of spice. Recently, a lot of the customers have been ordering very mild curries and the chefs have been having to throw away some wasted ingredients. To reduce cost and food wastage, the curry house starts monitoring how many ingredients are actually being used and changes their spending accordingly. The curry house needs 3 peppers for very spicy curries, 2 peppers for spicy curries, and only 1 pepper for mild curries. After adjusting their purchasing, the curry house now buys the exact amount of peppers they need. Previously, the curry house was buying enough peppers for 30 very spicy curries, 30 spicy curries, and 10 mild curries. They now buy enough peppers for 15 spicy curries and 90 mild curries. They no longer sell very spicy curries. How many fewer peppers does the curry house now buy?"""
    peppers_for_very_spicy = 3 * 30
    peppers_for_spicy = 2 * 30
    peppers_for_mild = 1 * 10
    total_peppers_before = peppers_for_very_spicy + peppers_for_spicy + peppers_for_mild
    peppers_for_spicy = 2 * 15
    peppers_for_mild = 1 * 90
    total_peppers_after = peppers_for_spicy + peppers_for_mild
    fewer_peppers = total_peppers_before - total_peppers_after
    result = fewer_peppers
    return result

print(solution())