def solution():
    initial_value = 4000  # Jocelyn bought the car 3 years ago at $4000
    depreciation_rate = 0.3  # The car's value has reduced by 30%
    current_value = initial_value * (1 - depreciation_rate) ** 3  # Calculate the current value after 3 years
    result = current_value
    return result

print(solution())