def solution():
    num_peaches = 250
    fresh_percentage = 0.6
    small_peaches = 15
    
    # Calculate the number of fresh peaches
    fresh_peaches = num_peaches * fresh_percentage
    
    # Subtract the number of small peaches
    fresh_peaches -= small_peaches
    
    result = fresh_peaches
    return result

print(solution())