def solution():
    capacity = 16  # in GB
    used_percentage = 50

    # Calculate the number of GB used
    used_space = (used_percentage / 100) * capacity

    # Calculate the number of GB still available
    available_space = capacity - used_space
    result = available_space
    return result

print(solution())