def solution():
    gym_budget = 0  # initialize gym budget variable
    num_dodgeballs = 0  # initialize number of dodgeballs variable
    
    # Calculate the new gym budget with a 20% increase
    gym_budget *= 1.2
    
    # Calculate the maximum number of softballs that can be bought with the new budget
    max_softballs = int(gym_budget / 9)
    
    result = max_softballs
    return result

print(solution())