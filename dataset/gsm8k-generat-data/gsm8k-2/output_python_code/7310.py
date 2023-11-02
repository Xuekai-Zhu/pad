def solution():
    """A superhero can use superhuman speed to run 10 miles in 4 minutes. The supervillain has an Evil-Mobile that drives 100 miles per hour. How many miles farther can the superhero run in an hour than the supervillain can drive?"""
    superhero_speed = 10 / 4  # miles per minute
    superhero_distance_in_hour = superhero_speed * 60
    villain_speed = 100  # miles per hour
    villain_distance_in_hour = villain_speed
    difference = superhero_distance_in_hour - villain_distance_in_hour
    result = difference
    return result

print(solution())