def solution():
    num_cows = 9
    
    # Calculate the number of goats Mr. Rainwater has using the ratio given
    num_goats = num_cows * 4
    
    # Calculate the number of chickens Mr. Rainwater has using the ratio given
    num_chickens = num_goats / 2
    
    result = num_chickens
    return result

print(solution())