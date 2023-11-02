def solution():
    # Calculate the available space in the jar
    available_space = 100 - 20 - 2*10  # 20 big toenails take twice the space of regular toenails

    # Calculate how many regular toenails can fit in the remaining space
    regular_toenails = available_space // 2

    result = regular_toenails
    return result

print(solution())