def solution():
    num_nose_sprays = 10
    cost_per_spray = 3

    # Calculate the total number of nose sprays Bob will receive with the promotion
    total_sprays = num_nose_sprays * 2

    # Calculate the total cost of all nose sprays Bob will receive
    total_cost = (total_sprays // 2) * cost_per_spray

    result = total_cost
    return result

print(solution())