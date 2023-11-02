def solution():
    total_bollards = 4000 * 2  # The company was contracted to install 4000 bollards on each side of the road
    installed_bollards = total_bollards * (3/4)  # The company was only able to install 3/4 of the required bollards

    # Calculate the remaining number of bollards to be installed
    remaining_bollards = total_bollards - installed_bollards
    result = remaining_bollards
    return result

print(solution())