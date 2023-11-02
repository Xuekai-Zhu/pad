def solution():
    # Calculate the distance the superhero can run in an hour
    distance_superhero = 10 * (60/4)  # the superhero can run 10 miles in 4 minutes, so in 1 hour they can run 10 * (60/4) = 150 miles
    # Calculate the distance the supervillain can drive in an hour
    distance_supervillain = 100
    # Calculate the difference in distance between the superhero and supervillain
    difference_distance = distance_superhero - distance_supervillain
    result = difference_distance
    return result

print(solution())