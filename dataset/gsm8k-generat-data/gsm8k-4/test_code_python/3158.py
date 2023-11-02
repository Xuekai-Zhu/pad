def solution():
    """Rex is taking lessons for his driver’s license. He wants to take 40 hour-long lessons 
    before his test, and decides to have two-hour sessions twice a week until he has done his test. 
    After 6 weeks, how many more weeks will Rex need to continue taking lessons to reach his goal?"""
    
    # Define the total number of lessons needed and the number of hours per lesson
    total_lessons = 40
    hours_per_lesson = 1

    # Define the number of hours that Rex can take lessons per week
    weekly_hours = 2 * 2  # two-hour sessions twice a week

    # Calculate the number of hours of lessons Rex has taken so far
    hours_taken = weekly_hours * 6  # 6 weeks have passed

    # Calculate the number of lessons Rex has already taken
    lessons_taken = hours_taken / hours_per_lesson

    # Calculate the number of lessons Rex still needs to take
    lessons_left = total_lessons - lessons_taken

    # Calculate the number of weeks Rex still needs to take lessons
    weeks_left = lessons_left / weekly_hours / 2  # divide by 2 because Rex takes 2 sessions per week

    result = weeks_left
    return result

print(solution())