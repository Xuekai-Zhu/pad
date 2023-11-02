def solution():
    """A store has an 8% discount on all items. If Shara paid $184 for a pair of shoes, how much did Shara save?"""
    # Define the original price and the discounted price
    original_price = None
    discounted_price = 184

    # Calculate the original price based on the discount
    discount_percent = 8
    original_price = discounted_price / (1 - discount_percent / 100)

    # Calculate the amount saved
    amount_saved = original_price - discounted_price

    # return the result
    result = amount_saved
    return result

print(solution())