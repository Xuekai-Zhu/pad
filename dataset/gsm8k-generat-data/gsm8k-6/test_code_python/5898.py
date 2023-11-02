def solution():
    # Calculate the total number of bollards required on all sides of the road
    total_bollards = 4000 * 2  # 4000 required on each side of the road

    # Calculate the number of bollards already installed
    installed_bollards = (3/4) * total_bollards

    # Calculate the number of bollards still required
    remaining_bollards = total_bollards - installed_bollards

    result = remaining_bollards
    return result

print(solution())