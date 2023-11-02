def solution():
    # Calculate the available space for the boats
    available_space = 42 - 4  # 4 feet of space are needed on both sides of the boats

    # Calculate the maximum number of boats that can fit
    max_boats = available_space // 3  # each boat is 3 feet across

    result = max_boats
    return result

print(solution())