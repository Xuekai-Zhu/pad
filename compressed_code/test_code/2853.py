def solution():
    
    drip_rate = 3 * 20/1000  
    pot_volume = 3  
    time_to_fill = pot_volume / drip_rate
    result = time_to_fill
    return result

print(solution())