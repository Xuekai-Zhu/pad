def solution():
    """If eight liters is 20% the capacity of a container filled with water, calculate the total capacity of 40 such containers filled with water."""
    # Define the ratio of 8 liters to the capacity of one container
    ratio = 0.2

    # Calculate the capacity of one container
    one_container_capacity = 8 / ratio

    # Calculate the total capacity of 40 containers
    total_capacity = one_container_capacity * 40

    # Return the result
    result = total_capacity
    return result

print(solution())