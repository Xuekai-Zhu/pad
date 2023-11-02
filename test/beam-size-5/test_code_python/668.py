def solution():
    
    total_good_days = 12
    total_bad_days = 12
    total_good_days = total_good_days - total_bad_days
    total_neutral_days = total_good_days - total_neutral_days
    good_days_left = total_good_days - 3 * good_days_left
    result = good_days_left
    return result

print(solution())