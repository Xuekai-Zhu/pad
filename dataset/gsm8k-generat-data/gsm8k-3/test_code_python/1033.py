def solution():
    """James takes up dancing for fitness.  He loses twice as many calories per hour as he did when he was walking.  He dances twice a day for .5 hours each time and he does this 4 times a week.  He burned 300 calories an hour walking.  How many calories does he lose a week from dancing?"""
    # Define the number of times James dances per week and the time he dances each time
    TIMES_DANCING = 2
    TIME_DANCING = 0.5

    # Define the number of calories James lost per hour when walking and dancing
    CALORIES_WALKING = 300
    CALORIES_DANCING = CALORIES_WALKING * 2

    # Calculate the total number of calories James loses from dancing each week
    calories_dancing_per_week = TIMES_DANCING * TIME_DANCING * CALORIES_DANCING * 4

    # Return the total number of calories James loses from dancing each week
    result = calories_dancing_per_week
    return result

print(solution())