def solution():
    ounces_needed = 80
    ounces_per_can = 8
    cost_per_can = 0.5
    total_cans = ounces_needed / ounces_per_can
    cost = total_cans * cost_per_can
    result = cost
    return result

print(solution())