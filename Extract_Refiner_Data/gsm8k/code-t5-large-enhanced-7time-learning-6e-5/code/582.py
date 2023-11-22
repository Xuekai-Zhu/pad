def solution():
    
    # Define the number of calories burned per hour
    AEROBIC_CALORIES_PER_HOUR = 500
    RUNNING_CALORIES_PER_HOUR = 600

    # Define the number of hours spent burning water
    AEROBIC_HOURS = 2
    RUNNING_HOURS = 1

    # Calculate the total calories burned
    total_calories_burned = AEROBIC_CALORIES_PER_HOUR * AEROBIC_HOURS + RUNNING_CALORIES_PER_HOUR * RUNNING_HOURS

    # Calculate the number of calories Hannah needs to drink
    calories_per_100_ml = 100

    # Calculate the total ml of water Hannah needs to drink
    total_water_ml = calories_per_100_ml * AEROBIC_HOURS * AEROBIC_HOURS + calories_per_100_ml

    # Display the total ml of water Hannah needs to drink
    result = total_water_ml
    return

print(solution())