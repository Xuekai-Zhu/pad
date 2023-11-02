def solution():
    num_roses = 80
    
    # Calculate the number of red roses
    num_red_roses = (3/4) * num_roses
    
    # Calculate the number of roses that are not red
    num_not_red_roses = num_roses - num_red_roses
    
    # Calculate the number of yellow roses
    num_yellow_roses = (1/4) * num_not_red_roses
    
    # Calculate the number of white roses
    num_white_roses = num_not_red_roses - num_yellow_roses
    
    # Calculate the total number of red and white roses
    num_red_or_white_roses = num_red_roses + num_white_roses
    
    result = num_red_or_white_roses
    return result

print(solution())