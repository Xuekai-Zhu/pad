def solution(): 
    brenda_score = 0
    david_score = 0
    
    # assume Brenda makes a 15-point play
    brenda_score += 15
    
    # Brenda is now ahead by 22 points
    brenda_score += 22
    
    # David makes a 32-point play
    david_score += 32
    
    # calculate Brenda's current score
    brenda_score += david_score
    
    # calculate the difference in score between Brenda and David
    score_difference = brenda_score - david_score
    
    result = score_difference
    return result

print(solution())