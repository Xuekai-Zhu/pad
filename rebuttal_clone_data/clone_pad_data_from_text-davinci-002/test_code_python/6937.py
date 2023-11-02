def solution():
    sugar_cost = 1.5
    salt_cost = 5.5 - (2 * sugar_cost)
    result = (sugar_cost * 3) + (salt_cost * 1)
    return result

print(solution())