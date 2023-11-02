def solution():
    # Define the variables
    distance_from_school = 5000
    popcorn_dropped_per_distance = 1 / 25
    squirrel_eaten_fraction = 1/4

    # Calculate the total popcorn dropped on the way home
    total_popcorn_dropped = distance_from_school * popcorn_dropped_per_distance

    # Calculate the fraction of popcorn remaining
    remaining_fraction = 1 - squirrel_eaten_fraction

    # Calculate the total remaining popcorn
    remaining_popcorn = total_popcorn_dropped * remaining_fraction

    result = remaining_popcorn
    return result

print(solution())