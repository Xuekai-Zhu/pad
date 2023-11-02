def solution():
    # Define the initial number of cows
    cow_count = 200
    
    # Calculate the number of calves born each year
    calf_count = cow_count / 2
    
    # After one year
    cow_count += calf_count
    cow_count += calf_count # Add the number of new calves
    
    # After two years
    cow_count += calf_count
    cow_count += calf_count # Add the number of new calves
    
    result = cow_count
    return result

print(solution())