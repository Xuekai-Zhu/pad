def solution():
    """Jasmine swims 12 laps every afternoon, Monday through Friday. How many laps does she swim in five weeks?"""
    # Define the number of laps Jasmine swims each day
    daily_laps = 12

    # Define the number of days in a week Jasmine swims
    weekly_days = 5

    # Calculate the number of laps Jasmine swims in a week
    weekly_laps = daily_laps * weekly_days

    # Calculate the number of laps Jasmine swims in five weeks
    five_weeks_laps = weekly_laps * 5

    # return the result
    result = five_weeks_laps
    return result

print(solution())