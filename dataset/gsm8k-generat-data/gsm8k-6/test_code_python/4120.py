def solution():
    # Find the number of shooting stars counted by Bridget, Reginald and Sam
    bridget_count = 14
    reginald_count = bridget_count - 2
    sam_count = reginald_count + 4

    # Find the average number of shooting stars observed by the three of them
    average_count = (bridget_count + reginald_count + sam_count) / 3

    # Find how many more shooting stars Sam counted than the average
    difference = sam_count - average_count
    result = difference
    return result

print(solution())