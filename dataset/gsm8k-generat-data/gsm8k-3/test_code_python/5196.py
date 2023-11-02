def solution():
    """Mark is reading books, for 2 hours each day. He decided to increase his time spent on reading books weekly, by 4 hours. How much time does Mark want to spend during one week on reading books?"""
    # Define the initial reading time per day
    INITIAL_TIME = 2

    # Define the increase in reading time per week
    INCREASE = 4

    # Calculate the total reading time per week
    total_time = 7 * INITIAL_TIME + INCREASE

    # Display the total reading time
    result = total_time
    return result

print(solution())