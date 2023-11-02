def solution():
    
    total_streetlights = 200
    total_squares = 15
    streetlights_per_square = 12
    used_streetlights = streetlights_per_square * total_squares
    unused_streetlights = total_streetlights - used_streetlights
    result = unused_streetlights
    return result

print(solution())