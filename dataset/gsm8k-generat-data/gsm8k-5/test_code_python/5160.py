def solution():
    lily_ducks = 20  # Lily bought 20 ducks
    lily_geese = 10  # Lily bought 10 geese
    rayden_ducks = 3 * lily_ducks  # Rayden bought three times as many ducks as Lily
    rayden_geese = 4 * lily_geese  # Rayden bought four times as many geese as Lily

    # Calculate the total ducks and geese bought by Rayden and Lily
    total_ducks = lily_ducks + rayden_ducks
    total_geese = lily_geese + rayden_geese

    # Calculate the difference in ducks and geese between Rayden and Lily
    difference_ducks = rayden_ducks - lily_ducks
    difference_geese = rayden_geese - lily_geese
    total_difference = difference_ducks + difference_geese
    
    result = total_difference
    return result

print(solution())