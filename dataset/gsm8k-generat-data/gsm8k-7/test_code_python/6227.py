def solution():
    flat_fee = 5.0
    weight = 5.0
    per_pound_cost = 0.8

    # Calculate the total shipping cost
    total_cost = flat_fee + (per_pound_cost * weight)
    result = total_cost
    return result

print(solution())