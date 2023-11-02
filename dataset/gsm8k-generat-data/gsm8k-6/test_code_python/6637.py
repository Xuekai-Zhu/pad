def solution():
    # Calculate the capacity of one container
    one_container_capacity = 8 / 0.2  # since 8 liters is 20% of the capacity, the total capacity is 8/0.2 = 40 liters

    # Calculate the total capacity of 40 such containers
    total_capacity = one_container_capacity * 40

    result = total_capacity
    return result

print(solution())