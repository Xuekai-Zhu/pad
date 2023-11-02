def solution():
    """Janet bought some muffins at the bakery. Each muffin is 75 cents. Janet paid $20 and got $11 in change back. How many muffins did Janet buy?"""
    # Define the price of each muffin
    muffin_price = 0.75

    # Calculate how much Janet spent on muffins
    spent_on_muffins = 20 - 11

    # Calculate the number of muffins Janet bought
    muffin_count = spent_on_muffins / muffin_price

    # Return the result
    result = int(muffin_count)
    return result

print(solution())