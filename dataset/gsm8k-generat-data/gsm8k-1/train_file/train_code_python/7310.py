def solution():
    """A superhero can use superhuman speed to run 10 miles in 4 minutes. The supervillain has an Evil-Mobile that drives 100 miles per hour. How many miles farther can the superhero run in an hour than the supervillain can drive?"""
    superhero_speed = 10 / (4 / 60)  # miles per hour
    supervillain_speed = 100  # miles per hour
    miles_more_superhero_can_run_in_hour = superhero_speed - supervillain_speed
    result = miles_more_superhero_can_run_in_hour
    return result

print(solution())