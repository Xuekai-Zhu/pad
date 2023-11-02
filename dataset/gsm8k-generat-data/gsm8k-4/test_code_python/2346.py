def solution():
    """John decides to trade in his stereo system. His old system cost 250 dollars and he got 80% of the value for it. He then buys a system that costs $600 that he gets a 25% discount on. How much money came out of his pocket?"""
    # Define the cost of John's old stereo
    old_stereo_cost = 250

    # Calculate the amount John received for trading in his old stereo
    trade_in_value = old_stereo_cost * 0.8

    # Define the cost of John's new stereo
    new_stereo_cost = 600

    # Calculate the discount on John's new stereo
    discount = new_stereo_cost * 0.25

    # Calculate the amount John paid for his new stereo
    final_cost = new_stereo_cost - discount

    # Calculate the total amount of money that came out of John's pocket
    total_cost = final_cost - trade_in_value

    # Return the result
    result = total_cost
    return result

print(solution())