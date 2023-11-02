def solution():
    """Marcy is the lunch monitor in an elementary school cafeteria. She gives 5 time-outs for running, 1 less than five times that number of time-outs for throwing food, and 1/3 the number of food-throwing time-outs for swearing. If each time-out is 5 minutes, how much time do the students spend in time-out total?"""
    running_time_outs = 5
    food_time_outs = (5 * running_time_outs) - 1
    swearing_time_outs = food_time_outs / 3
    total_time_outs = running_time_outs + food_time_outs + swearing_time_outs
    time_in_minutes = total_time_outs * 5
    result = time_in_minutes
    return result

print(solution())