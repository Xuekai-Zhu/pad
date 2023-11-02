def solution():
    # Calculate the total hours the 5th grade needs to read in order to beat the 6th grade by 1 hour
    total_hours = 299 + 1

    # Calculate the number of hours each 5th grade student needs to read per day to beat the 6th grade by 1 hour
    hours_per_day = total_hours / (20 * 7)  # 20 students and 7 days in a week
    result = hours_per_day
    return result

print(solution())