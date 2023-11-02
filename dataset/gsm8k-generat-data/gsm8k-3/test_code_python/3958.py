def solution():
    """It's Mother's day, so mothers get a 10% discount on the department store. Mothers who have 3 children or more can get an additional 4% off the discounted price. If Mrs. Brown has 4 children and wants to buy a pair of shoes that costs $125, how much will she pay?"""
    # Define the initial price of the shoes
    price = 125

    # Calculate the discount for Mother's Day
    discount = price * 0.1

    # Calculate the discounted price
    discounted_price = price - discount

    # Check if Mrs. Brown has 3 or more children
    if 4 >= 3:
        # Calculate the additional discount
        additional_discount = discounted_price * 0.04
        # Calculate the final price
        final_price = discounted_price - additional_discount
    else:
        # Mrs. Brown doesn't qualify for the additional discount
        final_price = discounted_price

    # Display the final price Mrs. Brown will pay
    result = final_price
    return result

print(solution())