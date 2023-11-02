def solution():
    initial_value = 4000
    depreciation_rate = 0.3  # 30% depreciation

    # Calculate the current value of the car
    current_value = initial_value * (1 - depreciation_rate)
    result = current_value
    return result

print(solution())