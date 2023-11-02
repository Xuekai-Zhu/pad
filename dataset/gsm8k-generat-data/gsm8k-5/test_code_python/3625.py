def solution():
    price_per_pound = 7  # A pound of steak costs $7
    pounds_bought = 2  # Ken buys two pounds of steak
    total_cost = price_per_pound * pounds_bought  # Calculate the total cost of the steak

    # Calculate the amount of money Ken will get back
    money_back = 20 - total_cost
    result = money_back
    return result

print(solution())