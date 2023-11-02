def solution():
    # Calculate the total money earned from cupcakes and cookies sales
    total_money = (50 * 2) + (40 * 0.5)

    # Calculate the cost of two basketballs
    basketball_cost = 2 * 40

    # Calculate the remaining money after buying the basketballs
    remaining_money = total_money - basketball_cost

    # Calculate the cost of each bottle of energy drink
    bottle_cost = remaining_money / 20
    result = bottle_cost
    return result

print(solution())