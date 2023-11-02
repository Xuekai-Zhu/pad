def solution():
    """Bridget counted 14 shooting stars in the night sky. Reginald counted two fewer shooting stars than did Bridget, but Sam counted four more shooting stars than did Reginald. How many more shooting stars did Sam count in the night sky than was the average number of shooting stars observed for the three of them?"""
    bridget_count = 14
    reginald_count = bridget_count - 2
    sam_count = reginald_count + 4
    total_count = bridget_count + reginald_count + sam_count
    average_count = total_count / 3
    difference = sam_count - average_count
    result = difference
    return result

print(solution())