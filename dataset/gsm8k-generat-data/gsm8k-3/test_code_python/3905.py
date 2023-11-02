def solution():
    """Jasmine swims 12 laps every afternoon, Monday through Friday. How many laps does she swim in five weeks?"""
    # Define the number of laps Jasmine swims each day
    laps_per_day = 12

    # Define the number of weekdays in a week
    weekdays_per_week = 5

    # Define the number of weeks
    weeks = 5

    # Calculate the total number of laps Jasmine swims in five weeks
    total_laps = laps_per_day * weekdays_per_week * weeks

    # Display the total number of laps
    result = total_laps
    return result

print(solution())