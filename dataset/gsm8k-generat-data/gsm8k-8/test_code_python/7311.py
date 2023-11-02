def solution():
    # Calculate the distance the superhero can run in an hour
    miles_per_minute = 10 / 4
    miles_per_hour = miles_per_minute * 60
    superhero_distance = miles_per_hour

    # Calculate the distance the supervillain can drive in an hour
    supervillain_distance = 100

    # Calculate the difference in distance
    distance_difference = superhero_distance - supervillain_distance
    result = distance_difference
    return result

print(solution())