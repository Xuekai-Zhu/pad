def solution():
    num_ducks = 25
    num_geese = 2*num_ducks - 10
    num_new_ducks = 4
    num_escaped_geese = 15 - 5

    # Add the new ducks to the total number of ducks
    total_ducks = num_ducks + num_new_ducks
    
    # Subtract the escaped geese from the total number of geese
    total_geese = num_geese - num_escaped_geese
    
    # Calculate the difference between the total number of geese and ducks
    difference = total_geese - total_ducks
    result = difference
    return result

print(solution())