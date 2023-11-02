def solution():
    """Jeremy buys 3 bags of chips for a party. Stacy and Emily also buy chips for the party. If they need 10 bags of chips total, and Stacy buys 4 bags, how many bags of chips should Emily buy?"""
    # Define the number of bags of chips bought by Jeremy and Stacy
    jeremy_chips = 3
    stacy_chips = 4

    # Calculate the number of bags of chips needed by Emily
    total_chips = 10
    emily_chips = total_chips - jeremy_chips - stacy_chips

    # return the result
    result = emily_chips
    return result

print(solution())