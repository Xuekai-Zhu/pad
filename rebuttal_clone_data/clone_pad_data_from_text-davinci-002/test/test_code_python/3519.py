def solution():
    shipping_cost = 5.00
    per_pound_cost = 0.80
    package_weight = 5
    total_cost = shipping_cost + (package_weight * per_pound_cost)
    result = total_cost
    return result

print(solution())