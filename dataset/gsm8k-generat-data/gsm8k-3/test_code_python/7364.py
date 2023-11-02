def solution():
    """Angelo and Melanie want to plan how many hours over the next week they should study together for their test next week. They have 2 chapters of their textbook to study and 4 worksheets to memorize. They figure out that they should dedicate 3 hours to each chapter of their textbook and 1.5 hours for each worksheet. If they plan to study no more than 4 hours each day, how many days should they plan to study total over the next week if they take a 10-minute break every hour, include 3 10-minute snack breaks each day, and 30 minutes for lunch each day?"""
    # Define the amount of time needed for each chapter and worksheet
    CHAPTER_TIME = 3
    WORKSHEET_TIME = 1.5

    # Calculate the total study time needed
    total_time = (CHAPTER_TIME * 2) + (WORKSHEET_TIME * 4)

    # Define the maximum study time per day
    MAX_STUDY_TIME = 4

    # Calculate the actual study time per day
    actual_study_time = MAX_STUDY_TIME - 0.5 - (3 * 0.17) - 0.5

    # Calculate the number of days needed to complete the studying
    num_days = total_time / actual_study_time

    # Round up to the next whole number of days
    num_days = int(num_days) + 1

    # Display the number of days needed
    result = num_days
    return result

print(solution())