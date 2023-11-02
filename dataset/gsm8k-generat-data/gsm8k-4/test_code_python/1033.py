def solution():
    """James takes up dancing for fitness. He loses twice as many calories per hour as he did when he was walking. He dances twice a day for .5 hours each time and he does this 4 times a week. He burned 300 calories an hour walking. How many calories does he lose a week from dancing?"""
    # Calculate the number of calories James burns per hour of dancing
    calories_per_hour = 2 * 300

    # Calculate the number of hours James dances per week
    hours_per_week = 2 * 0.5 * 4

    # Calculate the total number of calories James burns per week from dancing
    total_calories = calories_per_hour * hours_per_week

    result = total_calories
    return result

print(solution())