def solution():
    """An auto shop has a part that Clark needs for $80. Clark buys 7 of them and got a discount. If Clark only had to pay $439, how much was the discount?"""
    # Define the cost per part and number of parts purchased
    PART_PRICE = 80
    NUM_PARTS = 7

    # Calculate the total cost without discount
    total_cost = PART_PRICE * NUM_PARTS

    # Calculate the discount amount
    discount = total_cost - 439

    # Display the discount amount
    result = discount
    return result

print(solution())