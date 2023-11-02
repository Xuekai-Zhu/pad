def solution():
    """Angelo and Melanie want to plan how many hours over the next week they should study together for their test next week. They have 2 chapters of their textbook to study and 4 worksheets to memorize. They figure out that they should dedicate 3 hours to each chapter of their textbook and 1.5 hours for each worksheet. If they plan to study no more than 4 hours each day, how many days should they plan to study total over the next week if they take a 10-minute break every hour, include 3 10-minute snack breaks each day, and 30 minutes for lunch each day?"""
    # Define the time required to study each chapter and worksheet
    chapter_time = 3
    worksheet_time = 1.5

    # Calculate the total time required to study all the chapters and worksheets
    total_time = (2 * chapter_time) + (4 * worksheet_time)

    # Define the maximum time available to study each day
    max_study_time = 4

    # Calculate the total time available to study over the week, accounting for breaks and meals
    total_available_time = (7 * (max_study_time * 60)) - (5 * 10) - (3 * (3 * 10)) - (3 * 30)

    # Calculate the number of days required to complete all the studying
    num_days = total_time / (total_available_time / 60)

    # Round up to the nearest integer to account for partial days
    num_days = math.ceil(num_days)

    # Return the result
    result = num_days
    return result

print(solution())