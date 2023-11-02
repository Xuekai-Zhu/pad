def solution():
    """A store sold a certain brand of jeans for $40. They only have few pairs of jeans left so they decided to give 10% discount on every two pairs of jeans bought by a customer at any one time. How much will a customer pay for 3 pairs of jeans?"""
    # Define the price of one pair of jeans
    price = 40

    # Calculate the price of 2 pairs of jeans after discount
    discount_price = price * 0.9 * 2

    # Calculate the price of the third pair of jeans
    third_price = price

    # Calculate the total price of 3 pairs of jeans
    total_price = discount_price + third_price

    # return the result
    result = total_price
    return result

print(solution())