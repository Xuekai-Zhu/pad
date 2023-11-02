def solution():
    """To make a shed in his backyard, Tom needs 1000 bricks. He can buy half of the bricks for 50% off of $.50. The other Half he needs to pay full price. How many dollars does Tom spend?"""
    # Define the number of bricks and the price per brick for the discounted half
    discounted_bricks = 500
    discounted_price = 0.25

    # Define the number of bricks and the price per brick for the non-discounted half
    non_discounted_bricks = 500
    non_discounted_price = 0.50

    # Calculate the total cost of the discounted and non-discounted bricks
    discounted_cost = discounted_bricks * discounted_price
    non_discounted_cost = non_discounted_bricks * non_discounted_price

    # Calculate the total cost of all the bricks
    total_cost = discounted_cost + non_discounted_cost

    result = total_cost
    return result

print(solution())