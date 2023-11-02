def solution():
    mechanic_cost = 350
    supermarket_cost = (mechanic_cost - 50) / 3  # calculate the cost at the supermarket

    total_cost = mechanic_cost + supermarket_cost
    result = total_cost
    return result

print(solution())