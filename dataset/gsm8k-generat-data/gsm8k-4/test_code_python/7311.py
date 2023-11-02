def solution():
    """A superhero can use superhuman speed to run 10 miles in 4 minutes. The supervillain has an Evil-Mobile that drives 100 miles per hour. How many miles farther can the superhero run in an hour than the supervillain can drive?"""
    # Calculate the distance the superhero can run in an hour
    superhero_distance = (10 * 60) / 4

    # Calculate the distance the supervillain can drive in an hour
    supervillain_distance = 100

    # Calculate the difference between the two distances
    distance_difference = superhero_distance - supervillain_distance

    # Return the result
    result = distance_difference
    return result

print(solution())