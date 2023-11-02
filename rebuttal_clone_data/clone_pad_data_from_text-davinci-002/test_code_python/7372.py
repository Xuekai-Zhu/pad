def solution():
    city_A = "A"
    city_B = "B"
    city_C = "C"
    city_D = "D"
    
    distance_AB = 100
    distance_BC = distance_AB + 50
    distance_CD = 2 * distance_BC
    
    total_distance = distance_AB + distance_BC + distance_CD
    
    result = total_distance
    
    return result

print(solution())