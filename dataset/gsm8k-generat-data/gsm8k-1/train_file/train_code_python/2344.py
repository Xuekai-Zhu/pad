def solution():
    """A curry house sells curries that have varying levels of spice. Recently, a lot of the customers have been ordering very mild curries and the chefs have been having to throw away some wasted ingredients. To reduce cost and food wastage, the curry house starts monitoring how many ingredients are actually being used and changes their spending accordingly. The curry house needs 3 peppers for very spicy curries, 2 peppers for spicy curries, and only 1 pepper for mild curries. After adjusting their purchasing, the curry house now buys the exact amount of peppers they need. Previously, the curry house was buying enough peppers for 30 very spicy curries, 30 spicy curries, and 10 mild curries. They now buy enough peppers for 15 spicy curries and 90 mild curries. They no longer sell very spicy curries. How many fewer peppers does the curry house now buy?"""
    peppers_for_very_spicy_curries = 30 * 3
    peppers_for_spicy_curries = 30 * 2
    peppers_for_mild_curries = 10 * 1
    
    peppers_needed_for_spicy_curries = 15 * 2
    peppers_needed_for_mild_curries = 90 * 1
    
    total_peppers_bought_before = peppers_for_very_spicy_curries + peppers_for_spicy_curries + peppers_for_mild_curries
    total_peppers_bought_after = peppers_needed_for_spicy_curries + peppers_needed_for_mild_curries
    
    difference = total_peppers_bought_before - total_peppers_bought_after
    
    result = difference
    return result

print(solution())