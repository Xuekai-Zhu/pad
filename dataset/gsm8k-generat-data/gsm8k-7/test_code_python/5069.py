def solution():
    sausages_per_package = 2
    num_packages = 3
    cost_per_pound = 4
    total_weight = sausages_per_package * num_packages

    # Calculate the total cost of all sausages that Jake buys
    total_cost = total_weight * cost_per_pound

    result = total_cost
    return result

print(solution())