def solution():
    
    dozens_per_5_min = 2
    chocolates_per_dozen = 12
    time_per_5_min = 5
    hours = 4

    chocolates_per_5_min = dozens_per_5_min * chocolates_per_dozen
    chocolates_per_min = chocolates_per_5_min / time_per_5_min
    chocolates_per_hour = chocolates_per_min * 60
    total_chocolates = chocolates_per_hour * hours

    result = total_chocolates
    return result

print(solution())