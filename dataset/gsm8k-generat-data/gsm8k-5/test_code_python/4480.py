def solution():
    # Total amount of cleaner used in the first 15 minutes
    cleaner_15 = 2 * 15  # 2 ounces per minute for 15 minutes

    # Total amount of cleaner used between 15 and 25 minutes
    cleaner_10 = 3 * 10  # 3 ounces per minute for 10 minutes

    # Total amount of cleaner used between 25 and 30 minutes
    cleaner_5 = 4 * 5  # 4 ounces per minute for 5 minutes

    # Total amount of cleaner used after 30 minutes
    total_cleaner = cleaner_15 + cleaner_10 + cleaner_5
    result = total_cleaner
    return result

print(solution())