def solution():
    """James watched 2 episodes of Jeopardy and 2 episodes of Wheel of Fortune. Jeopardy is 20 minutes and Wheel of Fortune is twice as long. How many hours did he watch TV?"""
    # Define the length of one episode of Jeopardy in minutes
    jeopardy_length = 20

    # Define the length of one episode of Wheel of Fortune in minutes
    wheel_of_fortune_length = jeopardy_length * 2

    # Define the total amount of time in minutes that James spent watching TV
    total_time_minutes = (2 * jeopardy_length) + (2 * wheel_of_fortune_length)

    # Convert the total time to hours
    total_time_hours = total_time_minutes / 60

    # return the result
    result = total_time_hours
    return result

print(solution())