def solution():
    num_weights = 10
    weight = 30
    increase_percentage = 0.2

    # Calculate the total weight of the weights without the technology
    total_regular_weight = num_weights * weight

    # Calculate the percentage increase in weight
    weight_increase = total_regular_weight * increase_percentage

    # Calculate the total weight of the weights with the technology
    total_weight_with_technology = total_regular_weight + weight_increase

    result = total_weight_with_technology
    return result

print(solution())