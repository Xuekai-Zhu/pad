def solution():
    # Calculate the number of ducks and geese Rayden bought
    ducks_rayden = 3 * 20  # Rayden bought three times as many ducks as Lily
    geese_rayden = 4 * 10  # Rayden bought four times as many geese as Lily

    # Calculate the total number of ducks and geese Rayden has more than Lily
    total_ducks = ducks_rayden - 20  # Rayden has 60 more ducks than Lily
    total_geese = geese_rayden - 10  # Rayden has 30 more geese than Lily
    result = total_ducks + total_geese
    return result

print(solution())