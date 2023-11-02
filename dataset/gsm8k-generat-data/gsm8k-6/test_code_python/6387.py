def solution():
    # Calculate the area of the rectangular floor and the square carpet
    area_floor = 10 * 8
    area_carpet = 4 * 4

    # Calculate the area of the uncovered part of the floor
    area_uncovered = area_floor % area_carpet
    result = area_uncovered
    return result

print(solution())