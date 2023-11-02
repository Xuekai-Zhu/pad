def solution():
    """Caprice is taking piano lessons. Her mother pays the teacher $10 for every half-hour of teaching her daughter. If Caprice is taking one lesson per week, and the lesson lasts 1 hour, how much money would the teacher earn in 5 weeks?"""
    # Define the cost per half-hour lesson
    COST_PER_LESSON = 10

    # Calculate the cost for one lesson
    lesson_cost = COST_PER_LESSON * 2

    # Calculate the cost for 5 lessons
    total_cost = lesson_cost * 5

    # Display the total cost
    result = total_cost
    return result

print(solution())