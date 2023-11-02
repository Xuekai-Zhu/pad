def solution():
    """Rayden bought three times as many ducks as Lily from the market. He also bought four times as many geese as Lily. If Lily bought 20 ducks and 10 geese, how many more ducks and geese do Rayden have more than Lily altogether?"""
    # Define the number of ducks and geese that Lily bought
    lily_ducks = 20
    lily_geese = 10

    # Calculate the number of ducks and geese that Rayden bought
    rayden_ducks = lily_ducks * 3
    rayden_geese = lily_geese * 4

    # Calculate the difference in the number of ducks and geese between Rayden and Lily
    ducks_difference = rayden_ducks - lily_ducks
    geese_difference = rayden_geese - lily_geese

    # Calculate the total difference in the number of ducks and geese
    total_difference = ducks_difference + geese_difference

    # Return the result
    result = total_difference
    return result

print(solution())