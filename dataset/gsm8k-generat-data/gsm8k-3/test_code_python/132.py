def solution():
    """James buys 5 packs of beef that are 4 pounds each. The price of beef is $5.50 per pound. How much did he pay?"""
    # Define the price per pound of beef and the number of packs purchased
    BEEF_PRICE = 5.5
    PACKS_PURCHASED = 5

    # Calculate the total weight of beef purchased
    total_weight = PACKS_PURCHASED * 4

    # Calculate the total cost of beef purchased
    total_cost = total_weight * BEEF_PRICE

    # Return the result
    result = total_cost
    return result

print(solution())