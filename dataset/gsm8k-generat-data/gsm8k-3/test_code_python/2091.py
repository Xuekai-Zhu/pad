def solution():
    """A store has an 8% discount on all items. If Shara paid $184 for a pair of shoes, how much did Shara save?"""
    # Define the original price of the shoes
    original_price = 0  # initialize original_price
    discounted_price = 184

    # Calculate the original price of the shoes
    original_price = discounted_price / (1 - 0.08)

    # Calculate the amount saved
    savings = original_price - discounted_price

    # Display the amount saved
    result = savings
    return result

print(solution())