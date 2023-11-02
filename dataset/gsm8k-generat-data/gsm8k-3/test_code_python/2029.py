def solution():
    """Jeremy buys 3 bags of chips for a party. Stacy and Emily also buy chips for the party. If they need 10 bags of chips total, and Stacy buys 4 bags, how many bags of chips should Emily buy?"""
    # Define the number of bags of chips Jeremy buys
    jeremy_bags = 3

    # Define the number of bags of chips Stacy buys
    stacy_bags = 4

    # Calculate the number of bags of chips Emily should buy
    emily_bags = 10 - jeremy_bags - stacy_bags

    # Display the number of bags of chips Emily should buy
    result = emily_bags
    return result

print(solution())