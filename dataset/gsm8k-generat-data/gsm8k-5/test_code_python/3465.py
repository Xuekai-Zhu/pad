def solution():
    # Calculate the total cost of the loaves of bread and cartons of orange juice
    cost_bread = 5 * 5  # 5 loaves of bread at $5 each
    cost_orange_juice = 4 * 2  # 4 cartons of orange juice at $2 each
    total_cost = cost_bread + cost_orange_juice

    # Calculate how much money Wyatt has left from the $74 his mother gave him
    money_left = 74 - total_cost
    result = money_left
    return result

print(solution())