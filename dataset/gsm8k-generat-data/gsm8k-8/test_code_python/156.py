def solution():
    sandwich_cost = 4
    juice_cost = 2 * sandwich_cost
    milk_cost = 0.75 * (sandwich_cost + juice_cost)

    total_cost = sandwich_cost + juice_cost + milk_cost
    result = total_cost
    return result

print(solution())