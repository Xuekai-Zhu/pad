def solution():
    # Calculate the total cost of the items purchased
    total_cost = 42 + 18 + 14  # cost of giant sheet, rope, propane tank and burner

    # Calculate the amount of money left for helium
    money_left = 200 - total_cost

    # Calculate the amount of helium they can buy
    helium_amount = money_left / 1.5  # helium costs $1.50 per ounce

    # Calculate the height the balloon can fly with the amount of helium they have
    height = helium_amount * 113  # for every ounce of helium, balloon can fly 113 feet higher

    result = height
    return result

print(solution())