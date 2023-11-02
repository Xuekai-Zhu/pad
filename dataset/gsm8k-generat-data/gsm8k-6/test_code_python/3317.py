def solution():
    # Calculate the maximum number of days Hazel can miss and still not have to take her exams
    max_missed_days = 180 * 0.05  # 5% of the school year is the maximum number of days a senior can miss to skip their exams
    remaining_missed_days = max_missed_days - 6  # Hazel has already missed 6 days
    result = remaining_missed_days
    return result

print(solution())