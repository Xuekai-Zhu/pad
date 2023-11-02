def solution():
    # Calculate the total hours Mike trained during the first week
    hours_first_week = 7 * 2  # Mike played a maximum of 2 hours per day, for 7 days

    # Calculate the total hours Mike trained during the second week
    hours_second_week = 7 * 3  # Mike increased the maximum time to 3 hours per day, for 7 days

    # Calculate the total hours Mike trained during the first two weeks
    total_hours = hours_first_week + hours_second_week
    result = total_hours
    return result

print(solution())