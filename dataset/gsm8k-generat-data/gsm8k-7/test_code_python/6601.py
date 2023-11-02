def solution():
    budget = 15
    cost_per_artichoke = 1.25
    num_artichokes = budget // cost_per_artichoke
    num_ounces = (num_artichokes // 3) * 5
    result = num_ounces
    return result

print(solution())