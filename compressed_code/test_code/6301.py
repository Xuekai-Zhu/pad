def solution():
    
    
    probability_of_losing_both = 0.7 * 0.5  
    
    
    probability_of_winning_both = 0.3 * 0.5  
    
    
    difference = abs(probability_of_losing_both - probability_of_winning_both) * 100
    
    result = difference
    return result

print(solution())