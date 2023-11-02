def solution():
    """From Monday to Friday, Elle practices piano for 30 minutes. On Saturday, she practices piano three times as much as on a weekday. There is no practice on Sunday. How many hours does Elle spend practicing piano each week?"""
    # Define the number of minutes Elle practices on a weekday
    weekday_minutes = 30

    # Calculate the number of minutes Elle practices on Saturday
    saturday_minutes = weekday_minutes * 3

    # Calculate the total number of minutes Elle practices in a week
    total_minutes = (weekday_minutes * 5) + saturday_minutes

    # Convert the total minutes to hours
    total_hours = total_minutes / 60

    # Round the result to two decimal places
    result = round(total_hours, 2)
    return result

print(solution())