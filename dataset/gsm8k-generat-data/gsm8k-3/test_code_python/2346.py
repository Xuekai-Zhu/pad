def solution():
    """John decides to trade in his stereo system.  His old system cost 250 dollars and he got 80% of the value for it.  He then buys a system that costs $600 that he gets a 25% discount on.  How much money came out of his pocket?"""
    # Calculate the value of John's old stereo system
    old_system_value = 250 * 0.8

    # Calculate the amount John paid for the new stereo system after the 25% discount
    new_system_price = 600 * 0.75

    # Calculate the total amount of money that came out of John's pocket
    total_cost = new_system_price - old_system_value

    # Display the total cost
    result = total_cost
    return result

print(solution())