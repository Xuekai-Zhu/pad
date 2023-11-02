def solution():
    """Jocelyn bought a car 3 years ago at $4000. If the car's value has reduced by 30%, calculate the current value of the car."""
    # Define the initial cost and the percentage decrease
    initial_cost = 4000
    decrease_percentage = 0.3

    # Calculate the decrease in value
    decrease_value = initial_cost * decrease_percentage

    # Calculate the current value of the car
    current_value = initial_cost - decrease_value

    result = current_value
    return result

print(solution())