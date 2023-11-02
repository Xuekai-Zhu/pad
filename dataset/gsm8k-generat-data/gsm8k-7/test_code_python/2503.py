def solution():
    initial_num_nephews = 50
    current_num_nephews = initial_num_nephews * 2
    vihaan_extra_nephews = 60
    
    # Calculate the total number of nephews Alden has now
    aldens_current_nephews = current_num_nephews
    
    # Calculate the total number of nephews Vihaan has now
    vihaans_current_nephews = aldens_current_nephews + vihaan_extra_nephews
    
    # Calculate the total number of nephews the two have altogether
    total_nephews = aldens_current_nephews + vihaans_current_nephews
    result = total_nephews
    return result

print(solution())