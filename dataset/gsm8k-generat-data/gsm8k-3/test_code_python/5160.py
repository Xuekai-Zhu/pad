def solution():
    """Rayden bought three times as many ducks as Lily from the market. He also bought four times as many geese as Lily. If Lily bought 20 ducks and 10 geese, how many more ducks and geese do Rayden have more than Lily altogether?"""
    # Determine the number of ducks and geese Lily bought
    lily_ducks = 20
    lily_geese = 10

    # Calculate the number of ducks and geese Rayden bought
    rayden_ducks = lily_ducks * 3
    rayden_geese = lily_geese * 4

    # Calculate the total difference in ducks and geese between Rayden and Lily
    duck_difference = rayden_ducks - lily_ducks
    goose_difference = rayden_geese - lily_geese
    total_difference = duck_difference + goose_difference

    # Display the total difference in ducks and geese
    result = total_difference
    return result

print(solution())