def solution():
    # Calculate the superhero's speed in miles per minute
    superhero_speed = 10 / 4  # 10 miles in 4 minutes

    # Calculate the superhero's speed in miles per hour
    superhero_speed *= 60  # Multiply by 60 to convert minutes to hours

    # Calculate the distance the superhero can run in one hour
    superhero_distance = superhero_speed * 1  # 1 hour

    # Calculate the distance the supervillain can drive in one hour
    supervillain_distance = 100 * 1  # 100 miles per hour for 1 hour

    # Calculate the difference in distance
    distance_difference = superhero_distance - supervillain_distance
    result = distance_difference
    return result

print(solution())