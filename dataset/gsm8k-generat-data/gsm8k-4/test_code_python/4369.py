def solution():
    """Rose bought a plant with a 10% discount. If the price is $10, how much did Rose pay after the discount?"""
    # Define the initial price of the plant and the discount percentage
    price = 10
    discount_percentage = 10

    # Calculate the discount amount
    discount_amount = price * (discount_percentage / 100)

    # Calculate the final price after the discount
    final_price = price - discount_amount

    # return the result
    result = final_price
    return result

print(solution())