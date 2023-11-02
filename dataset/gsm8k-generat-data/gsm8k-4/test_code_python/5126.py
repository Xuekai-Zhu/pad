def solution():
    """Micheal decided to take some piano lessons. One lesson costs $30 and lasts for 1.5 hours. How much will Micheal need to pay for 18 hours of lessons?"""
    # Define the cost per lesson and the length of a lesson
    LESSON_COST = 30
    LESSON_LENGTH = 1.5

    # Calculate the total number of lessons needed for 18 hours
    total_lessons = 18 / LESSON_LENGTH

    # Calculate the total cost of the lessons
    total_cost = total_lessons * LESSON_COST

    # Return the result
    result = total_cost
    return result

print(solution())