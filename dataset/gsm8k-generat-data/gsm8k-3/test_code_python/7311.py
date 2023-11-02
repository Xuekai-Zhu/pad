def solution():
    """
    A superhero can use superhuman speed to run 10 miles in 4 minutes.
    The supervillain has an Evil-Mobile that drives 100 miles per hour.
    How many miles farther can the superhero run in an hour than the supervillain can drive?
    """
    # Convert superhero's speed to miles per hour
    superhero_speed = 10 * 60 / 4  # 10 miles in 4 minutes, multiplied by 15 to get miles per hour

    # Calculate the distance the superhero can run in an hour
    superhero_distance = superhero_speed * 1  # 1 hour

    # Calculate the distance the supervillain can drive in an hour
    supervillain_distance = 100 * 1  # 100 miles per hour for 1 hour

    # Calculate the difference in distance between the superhero and supervillain
    distance_difference = superhero_distance - supervillain_distance

    # Display the result
    result = distance_difference
    return result

print(solution())