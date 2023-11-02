def solution():
    initial_legos = 380  # Nellie initially had 380 legos
    lost_legos = 57  # Nellie lost 57 legos
    sister_legos = 24  # Nellie gave her sister 24 legos
    
    # Calculate the total number of legos Nellie has now
    total_legos = initial_legos - lost_legos - sister_legos
    result = total_legos
    return result

print(solution())