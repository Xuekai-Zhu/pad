def solution():
    # Find the percentage of kernels that pop in each bag
    percentage1 = (60 / 75) * 100
    percentage2 = (42 / 50) * 100
    percentage3 = (82 / 100) * 100

    # Find the average percentage of kernels that pop in all three bags
    average_percentage = (percentage1 + percentage2 + percentage3) / 3
    result = average_percentage
    return result

print(solution())