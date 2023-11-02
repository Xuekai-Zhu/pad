def solution():
    tents_north = 100
    tents_east = tents_north * 2
    tents_center = tents_north * 4
    tents_south = 200
    total_tents = tents_north + tents_east + tents_center + tents_south
    result = total_tents
    return result

print(solution())