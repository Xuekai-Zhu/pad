def solution():
    """Adam needs a new laptop and has two choices. The first laptop is $500, and the second laptop is 3 times as costly as the first laptop. How much would Adam have to spend if he decides to buy both?"""
    # Define the price of the first laptop
    laptop1_price = 500

    # Define the price of the second laptop
    laptop2_price = laptop1_price * 3

    # Calculate the total cost
    total_cost = laptop1_price + laptop2_price

    # Return the total cost
    result = total_cost
    return result

print(solution())