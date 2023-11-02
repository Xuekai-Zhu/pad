def solution():
    bridget_count = 14  # Bridget counted 14 shooting stars
    reginald_count = bridget_count - 2  # Reginald counted 2 fewer shooting stars than Bridget
    sam_count = reginald_count + 4  # Sam counted 4 more shooting stars than Reginald
    total_count = bridget_count + reginald_count + sam_count  # Total number of shooting stars observed

    # Calculate the average number of shooting stars observed by the three of them
    average_count = total_count / 3

    # Calculate how many more shooting stars Sam counted than the average
    difference = sam_count - average_count
    result = difference
    return result

print(solution())