def solution():
    original_value = 4000
    depreciation_rate = 0.3

    # Calculate the reduction in value after 3 years
    reduction = original_value * depreciation_rate * 3

    # Calculate the current value of the car
    current_value = original_value - reduction
    result = current_value
    return result

print(solution())