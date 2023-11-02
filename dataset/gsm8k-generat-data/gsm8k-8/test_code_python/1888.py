def solution():
    total_streetlights = 200
    total_squares = 15
    streetlights_per_square = 12

    streetlights_used = total_squares * streetlights_per_square
    streetlights_unused = total_streetlights - streetlights_used

    result = streetlights_unused
    return result

print(solution())