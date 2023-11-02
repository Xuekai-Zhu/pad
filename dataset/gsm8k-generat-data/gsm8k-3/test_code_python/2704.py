def solution():
    """Jocelyn bought a car 3 years ago at $4000. If the car's value has reduced by 30%, calculate the current value of the car."""
    # Define the initial cost of the car
    initial_cost = 4000

    # Calculate the reduction in value after 3 years
    reduction = 0.3 * initial_cost

    # Calculate the current value of the car
    current_value = initial_cost - reduction

    # Display the current value of the car
    result = current_value
    return result

print(solution())