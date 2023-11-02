def solution():
    """To make a shed in his backyard, Tom needs 1000 bricks. He can buy half of the bricks for 50% off of $.50. The other Half he needs to pay full price. How many dollars does Tom spend?"""
    # Define the number of bricks Tom needs and the full price per brick
    BRICKS_NEEDED = 1000
    FULL_PRICE = 0.50

    # Calculate the number of bricks Tom can buy at a discount and the cost
    discount_bricks = BRICKS_NEEDED // 2
    discount_cost = discount_bricks * FULL_PRICE * 0.5

    # Calculate the number of bricks Tom needs to buy at full price and the cost
    full_price_bricks = BRICKS_NEEDED - discount_bricks
    full_price_cost = full_price_bricks * FULL_PRICE

    # Calculate the total cost
    total_cost = discount_cost + full_price_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())