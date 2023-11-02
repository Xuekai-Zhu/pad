def solution():
    """Ralph watches TV for 4 hours a day from Monday to Friday, and 6 hours a day on Saturday and Sunday. How many hours does Ralph spend watching TV in one week?"""
    
    # Calculate the number of hours Ralph watches TV from Monday to Friday
    weekday_hours = 4 * 5

    # Calculate the number of hours Ralph watches TV on Saturday and Sunday
    weekend_hours = 6 * 2

    # Calculate the total number of hours Ralph watches TV in a week
    total_hours = weekday_hours + weekend_hours

    result = total_hours
    return result

print(solution())