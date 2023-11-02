def solution():
    """Rex is taking lessons for his driver’s license. He wants to take 40 hour-long lessons before his test, and decides to have two-hour sessions twice a week until he has done his test. After 6 weeks, how many more weeks will Rex need to continue taking lessons to reach his goal?"""
    # Define the number of hours Rex wants to take lessons for
    goal_hours = 40

    # Define the length of each lesson in hours
    lesson_length = 2

    # Define the number of lessons Rex takes per week
    lessons_per_week = 2

    # Calculate the total number of hours Rex has already taken
    hours_taken = lessons_per_week * lesson_length * 6

    # Calculate the remaining number of hours Rex needs to take
    hours_remaining = goal_hours - hours_taken

    # Calculate the number of weeks Rex needs to continue taking lessons for
    weeks_remaining = hours_remaining / (lessons_per_week * lesson_length)

    # Display the number of weeks Rex needs to continue taking lessons for
    result = weeks_remaining
    return result

print(solution())