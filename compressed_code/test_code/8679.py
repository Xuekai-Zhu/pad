def solution():
    
    hand_crank_time = 45 
    electric_time = 20 
    total_time = 6 * 60 
    pencils_hand_crank = total_time // hand_crank_time
    pencils_electric = total_time // electric_time
    difference = pencils_electric - pencils_hand_crank
    result = difference
    return result

print(solution())