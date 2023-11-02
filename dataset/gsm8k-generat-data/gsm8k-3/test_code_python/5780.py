def solution():
    """Travis wants to fly to Australia. The regular tickets cost about $2000. As Travis is a student, he will get a 30% discount on this price. How much does he need to pay for his ticket?"""
    # Define the regular price and discount percentage
    REGULAR_PRICE = 2000
    DISCOUNT_PERCENTAGE = 0.3

    # Calculate Travis's discount
    discount = REGULAR_PRICE * DISCOUNT_PERCENTAGE

    # Calculate the price Travis needs to pay
    price = REGULAR_PRICE - discount

    # Display the price Travis needs to pay
    result = price
    return result

print(solution())