def solution():
    # Find the initial number of tadpoles
    tadpoles = 3 * 50 

    # Calculate the new number of fish and tadpoles after Curtis caught 7 fish and half the tadpoles developed into frogs
    new_fish = 50 - 7  
    new_tadpoles = tadpoles / 2  

    # Calculate the difference between the new number of tadpoles and fish
    tadpoles_minus_fish = new_tadpoles - new_fish  
    result = tadpoles_minus_fish
    return result

print(solution())