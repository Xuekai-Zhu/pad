def solution():
    peaches_cost = 2  # The cost of 1 pound of peaches is $2
    peaches_quantity = 3  # Ines bought 3 pounds of peaches
    purse_money = 20  # Ines had $20 in her purse

    # Calculate the total cost of the peaches
    total_cost = peaches_cost * peaches_quantity

    # Calculate how much money Ines had left after buying the peaches
    money_left = purse_money - total_cost
    result = money_left
    return result

print(solution())