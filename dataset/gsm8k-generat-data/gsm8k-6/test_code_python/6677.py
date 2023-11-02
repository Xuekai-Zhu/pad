def solution():
    # Calculate the number of flowers Justin needs to collect
    num_flowers = 30
    
    # Calculate the time Justin has spent gathering flowers in minutes
    time_spent = 2 * 60
    
    # Calculate the number of flowers Justin lost
    lost_flowers = 3
    
    # Calculate the total number of flowers Justin needs to have
    total_flowers = num_flowers + lost_flowers
    
    # Calculate the total time Justin needs to find all the flowers
    total_time = total_flowers * 10
    
    # Calculate the additional time Justin needs to look for flowers
    additional_time = total_time - time_spent
    
    result = additional_time
    return result

print(solution())