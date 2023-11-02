def solution():
    
    bridget_count = 14
    reginald_count = bridget_count - 2
    sam_count = reginald_count + 4
    total_count = bridget_count + reginald_count + sam_count
    average_count = total_count / 3
    difference = sam_count - average_count
    result = difference
    return result

print(solution())