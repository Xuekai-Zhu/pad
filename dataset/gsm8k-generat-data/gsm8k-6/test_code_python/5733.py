def solution():
    # Calculate the number of marbles Gideon has
    num_marbles = 100  # a century has 100 years
    
    # Calculate the number of marbles Gideon has left after giving 3/4 to his sister
    num_marbles_left = (1/4) * num_marbles
    
    # Calculate Gideon's age five years from now, when he multiplies his remaining marbles by 2
    age = 2 * num_marbles_left + 5
    
    # Calculate Gideon's current age
    current_age = age - 5
    
    result = current_age
    return result

print(solution())