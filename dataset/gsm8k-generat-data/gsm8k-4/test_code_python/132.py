def solution():
    """James buys 5 packs of beef that are 4 pounds each. The price of beef is $5.50 per pound. How much did he pay?"""
    # Define the weight of each pack and the price per pound
    pack_weight = 4
    price_per_pound = 5.5

    # Calculate the total weight of the beef
    total_weight = pack_weight * 5

    # Calculate the total cost of the beef
    total_cost = total_weight * price_per_pound

    # Return the result
    result = total_cost
    return result

print(solution())