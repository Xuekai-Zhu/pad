def solution():
    """Marcel bought a pen for $4, and a briefcase for five times the price. How much did Marcel pay for both items?"""
    # Define the price of the pen and the multiplier for the briefcase
    pen_price = 4
    briefcase_multiplier = 5

    # Calculate the price of the briefcase
    briefcase_price = briefcase_multiplier * pen_price

    # Calculate the total cost of both items
    total_cost = pen_price + briefcase_price

    # return the result
    result = total_cost
    return result

print(solution())