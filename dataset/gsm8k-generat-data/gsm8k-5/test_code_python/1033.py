def solution():
    calories_per_hour_walking = 300  # James burns 300 calories per hour when walking
    calories_per_hour_dancing = 2 * calories_per_hour_walking  # James loses twice as many calories per hour when dancing

    # Calculate the total number of calories James burns per day from dancing
    calories_per_day = calories_per_hour_dancing * 0.5 * 2

    # Calculate the total number of calories James burns per week from dancing
    calories_per_week = calories_per_day * 4
    result = calories_per_week
    return result

print(solution())