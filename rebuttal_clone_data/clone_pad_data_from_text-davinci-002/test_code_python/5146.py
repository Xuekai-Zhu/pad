def solution():
    cost_per_bagel = 2.25
    cost_per_dozen = 24
    savings_per_bagel = (cost_per_dozen / 12) - cost_per_bagel
    result = savings_per_bagel
    return result

print(solution())