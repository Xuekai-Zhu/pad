def solution():
    """It's Mother's day, so mothers get a 10% discount on the department store. Mothers who have 3 children or more can get an additional 4% off the discounted price. If Mrs. Brown has 4 children and wants to buy a pair of shoes that costs $125, how much will she pay?"""
    # Define the initial price of the shoes
    shoes_price = 125

    # Calculate the price with the 10% Mother's day discount
    discounted_price = shoes_price * 0.9

    # Check if Mrs. Brown has 3 or more children
    num_children = 4  # Mrs. Brown has 4 children
    if num_children >= 3:
        # Calculate the additional 4% discount
        additional_discount = discounted_price * 0.04
        final_price = discounted_price - additional_discount
    else:
        final_price = discounted_price

    result = final_price
    return result

print(solution())