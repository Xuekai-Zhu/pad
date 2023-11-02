def solution():
    cost_now = 1800 / (1 - 2/5)  # Calculate the current cost of the lawnmower using the proportion
    cost_4_lawnmowers = 4 * cost_now  # Calculate the cost of buying 4 lawnmowers
    result = cost_4_lawnmowers
    return result

print(solution())