def solution():
    max_toenails = 100
    big_toenails = 20
    regular_toenails = 40
    big_toenail_space = 2  # takes up twice as much space as regular toenail

    # Calculate the remaining space in the jar after adding big and regular toenails
    remaining_space = max_toenails - (big_toenails + regular_toenails * big_toenail_space)

    # Calculate the number of regular toenails that can fit in the remaining space
    num_regular_toenails = remaining_space

    result = num_regular_toenails
    return result

print(solution())