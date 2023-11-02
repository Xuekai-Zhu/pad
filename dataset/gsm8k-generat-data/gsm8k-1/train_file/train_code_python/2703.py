def solution():
    """Jocelyn bought a car 3 years ago at $4000. If the car's value has reduced by 30%, calculate the current value of the car."""
    initial_value = 4000
    percent_reduction = 30
    reduction_amount = initial_value * (percent_reduction / 100)
    current_value = initial_value - reduction_amount
    result = current_value
    return result

print(solution())