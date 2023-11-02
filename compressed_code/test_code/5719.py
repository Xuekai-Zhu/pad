def solution():
    
    north_tents = 100
    east_tents = 2 * north_tents
    center_tents = 4 * north_tents
    south_tents = 200
    total_tents = north_tents + east_tents + center_tents + south_tents
    result = total_tents
    return result

print(solution())