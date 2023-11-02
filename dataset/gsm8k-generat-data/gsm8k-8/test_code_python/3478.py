def solution():
    # Calculate the total number of S'mores needed
    total_smores = 3 * 8

    # Calculate the number of supplies needed to make one S'more
    supplies_per_smores = 4 / 1  # 4 S'mores cost $3

    # Calculate the total cost of all the supplies
    total_cost = (supplies_per_smores * total_smores) / 3  # 3 S'mores each

    result = total_cost
    return result

print(solution())