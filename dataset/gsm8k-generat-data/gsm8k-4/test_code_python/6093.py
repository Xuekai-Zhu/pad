def solution():
    """During my workout yesterday, I did 30 squats. Each day, I plan to increase my number of squats by 5 more than the previous day. If I do my workout for four consecutive days, how many squats will I perform the day after tomorrow?"""
    # Define the number of squats performed on the first day and the increment
    initial_squats = 30
    increment = 5

    # Calculate the number of squats to perform on each day
    day1_squats = initial_squats
    day2_squats = day1_squats + increment
    day3_squats = day2_squats + increment
    day4_squats = day3_squats + increment

    # Calculate the number of squats to perform the day after tomorrow
    day_after_tomorrow_squats = day3_squats + increment

    # return the result
    result = day_after_tomorrow_squats
    return result

print(solution())