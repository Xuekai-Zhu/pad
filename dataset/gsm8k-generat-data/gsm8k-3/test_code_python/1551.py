def solution():
    """Marcy is the lunch monitor in an elementary school cafeteria. She gives 5 time-outs for running, 1 less than five times that number of time-outs for throwing food, and 1/3 the number of food-throwing time-outs for swearing. If each time-out is 5 minutes, how much time do the students spend in time-out total?"""
    # Define the number of time-outs for running
    running_timeouts = 5

    # Define the number of time-outs for throwing food
    food_timeouts = (5 * running_timeouts) - 1

    # Define the number of time-outs for swearing
    swearing_timeouts = food_timeouts / 3

    # Calculate the total number of time-outs
    total_timeouts = running_timeouts + food_timeouts + swearing_timeouts

    # Calculate the total time spent in time-out
    total_time = total_timeouts * 5

    # Display the total time spent in time-out
    result = total_time
    return result

print(solution())