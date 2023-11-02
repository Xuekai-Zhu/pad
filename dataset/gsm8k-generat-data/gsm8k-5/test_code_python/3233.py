def solution():
    # Calculate the percentage of popped kernels in the first bag
    percent_popped_1 = (60/75) * 100

    # Calculate the percentage of popped kernels in the second bag
    percent_popped_2 = (42/50) * 100

    # Calculate the percentage of popped kernels in the third bag
    percent_popped_3 = (82/100) * 100

    # Calculate the average percentage of popped kernels across all bags
    average_percent_popped = (percent_popped_1 + percent_popped_2 + percent_popped_3) / 3
    result = average_percent_popped
    return result

print(solution())