def solution():
    # Calculate the initial number of geese
    initial_geese = 2*25 - 10

    # Calculate the total number of birds after the small flock of ducks arrived
    total_birds = 25 + 4 + initial_geese

    # Calculate the number of geese that leave the park
    geese_leave = 15 - 5

    # Calculate the number of geese and ducks remaining after the geese leave
    remaining_geese = initial_geese - geese_leave
    remaining_ducks = 25 + 4

    # Calculate the difference between the number of remaining geese and ducks
    difference = remaining_geese - remaining_ducks

    result = difference
    return result

print(solution())