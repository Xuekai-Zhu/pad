def solution():
    
    sarah_speeding = 6
    mark_speeding = sarah_speeding
    mark_parking = 2 * (24 - sarah_speeding - mark_speeding) / 3
    result = mark_parking
    return result

print(solution())