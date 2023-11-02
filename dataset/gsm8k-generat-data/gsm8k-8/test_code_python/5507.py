def solution():
    weight_capacity = 1000
    safety_margin = 0.2
    john_weight = 250

    weight_allowed = (weight_capacity * (1 - safety_margin)) - john_weight
    result = weight_allowed
    return result

print(solution())