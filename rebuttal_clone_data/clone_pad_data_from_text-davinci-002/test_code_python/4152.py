def solution():
    cost1 = 300
    life1 = 15
    cost2 = 120
    life2 = 5
    total_life = life1 + life2
    number_of_coats = 30 / total_life
    total_cost1 = cost1 * number_of_coats
    total_cost2 = cost2 * number_of_coats
    savings = total_cost1 - total_cost2
    result = savings
    return result

print(solution())