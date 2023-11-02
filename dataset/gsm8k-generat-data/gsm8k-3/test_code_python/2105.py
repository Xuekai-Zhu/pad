def solution():
    """Tom decides to take 10 dance lessons that cost $10 each, but he gets two of them for free. How much does he pay?"""
    # Define the cost per dance lesson and the number of free lessons
    COST_PER_LESSON = 10
    NUM_FREE_LESSONS = 2

    # Calculate the total cost of the dance lessons
    num_paid_lessons = 10 - NUM_FREE_LESSONS
    total_cost = num_paid_lessons * COST_PER_LESSON

    # Display the total cost
    result = total_cost
    return result

print(solution())