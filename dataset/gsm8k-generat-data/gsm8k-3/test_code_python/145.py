def solution():
    """James watched 2 episodes of Jeopardy and 2 episodes of Wheel of Fortune. Jeopardy is 20 minutes and Wheel of Fortune is twice as long. How many hours did he watch TV?"""
    # Define the length of Jeopardy episodes in minutes
    JEOPARDY_LENGTH = 20

    # Define the length of Wheel of Fortune episodes in minutes
    WHEEL_OF_FORTUNE_LENGTH = JEOPARDY_LENGTH * 2

    # Calculate the total length of time watched in minutes
    total_time_minutes = (2 * JEOPARDY_LENGTH) + (2 * WHEEL_OF_FORTUNE_LENGTH)

    # Convert the total time to hours
    total_time_hours = total_time_minutes / 60

    # Return the result
    result = total_time_hours
    return result

print(solution())