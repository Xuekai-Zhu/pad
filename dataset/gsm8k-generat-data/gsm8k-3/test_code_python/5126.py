def solution():
    """Micheal decided to take some piano lessons. One lesson costs $30 and lasts for 1.5 hours. How much will Micheal need to pay for 18 hours of lessons?"""
    # Define the cost and duration of one lesson
    LESSON_COST = 30
    LESSON_DURATION = 1.5

    # Calculate the number of lessons needed for 18 hours of lessons
    num_lessons = 18 / LESSON_DURATION

    # Calculate the total cost of the lessons
    total_cost = num_lessons * LESSON_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())