def solution():
    """A curry house sells curries that have varying levels of spice. Recently, a lot of the customers have been ordering very mild curries and the chefs have been having to throw away some wasted ingredients. To reduce cost and food wastage, the curry house starts monitoring how many ingredients are actually being used and changes their spending accordingly. The curry house needs 3 peppers for very spicy curries, 2 peppers for spicy curries, and only 1 pepper for mild curries. After adjusting their purchasing, the curry house now buys the exact amount of peppers they need. Previously, the curry house was buying enough peppers for 30 very spicy curries, 30 spicy curries, and 10 mild curries. They now buy enough peppers for 15 spicy curries and 90 mild curries. They no longer sell very spicy curries. How many fewer peppers does the curry house now buy?"""
    # Define the number of peppers needed for each type of curry
    VERY_SPICY_PEPPERS = 3
    SPICY_PEPPERS = 2
    MILD_PEPPERS = 1

    # Calculate the total number of peppers needed previously
    previous_peppers = (30 * VERY_SPICY_PEPPERS) + (30 * SPICY_PEPPERS) + (10 * MILD_PEPPERS)

    # Calculate the total number of peppers needed now
    new_peppers = (15 * SPICY_PEPPERS) + (90 * MILD_PEPPERS)

    # Calculate the difference in the number of peppers needed
    difference = previous_peppers - new_peppers

    # Display the number of fewer peppers needed
    result = difference
    return result

print(solution())