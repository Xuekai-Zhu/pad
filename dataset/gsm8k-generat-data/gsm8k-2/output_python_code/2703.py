def solution():
    """Jocelyn bought a car 3 years ago at $4000. If the car's value has reduced by 30%, calculate the current value of the car."""
    original_value = 4000
    depreciation_rate = 0.3
    current_value = original_value - original_value * depreciation_rate
    result = current_value
    return result

print(solution())