def solution():
    # Total number of positive cases on the first day
    day1_cases = 2000

    # Number of positive cases on the second day
    day2_cases = day1_cases + 500 - 50

    # Number of positive cases on the third day
    day3_cases = day2_cases + 1500 - 200

    # Total number of positive cases after the third day
    total_cases = day3_cases
    result = total_cases
    return result

print(solution())