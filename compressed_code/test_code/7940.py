def solution():
    
    trumpet_weight = 5
    clarinet_weight = 5
    trombone_weight = 10
    tuba_weight = 20
    drum_weight = 15
    
    total_trumpet_weight = 6 * trumpet_weight
    total_clarinet_weight = 9 * clarinet_weight
    total_trombone_weight = 8 * trombone_weight
    total_tuba_weight = 3 * tuba_weight
    total_drum_weight = 2 * drum_weight
    
    total_weight = (total_trumpet_weight + total_clarinet_weight + 
                    total_trombone_weight + total_tuba_weight + total_drum_weight)
    
    result = total_weight
    return result

print(solution())