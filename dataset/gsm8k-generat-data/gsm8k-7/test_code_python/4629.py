def solution():
    num_bottles = 3
    price = 1.5

    # Calculate the cost per bottle
    cost_per_bottle = price / num_bottles

    # Calculate the cost of four bottles
    total_cost = cost_per_bottle * 4
    result = total_cost
    return result

print(solution())