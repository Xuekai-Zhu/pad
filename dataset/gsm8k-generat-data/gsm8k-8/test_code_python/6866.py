def solution():
    # Define the number of mallard ducks
    mallard_ducks = 25

    # Define the number of geese
    geese = 2 * mallard_ducks - 10

    # Add the small flock of ducks
    total_ducks = mallard_ducks + 4

    # Calculate the number of geese remaining
    remaining_geese = geese - (15 - 5)

    # Calculate the difference between the number of geese and ducks
    diff = remaining_geese - total_ducks
    
    result = diff
    return result

print(solution())