def solution():
    
    total_spots = 30 * 2  
    back_spots = total_spots / 3
    torso_spots = 30
    side_spots = total_spots - back_spots - torso_spots
    result = side_spots
    return result

print(solution())