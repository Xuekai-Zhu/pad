def solution():
    area_carpet = 4 ** 2  # area of the square carpet is 4*4=16 sq.m
    area_floor = 10 * 8  # area of the rectangular floor is 10*8=80 sq.m

    # calculate the total number of carpets required to cover the floor
    num_carpets = (area_floor + area_carpet - 1) // area_carpet

    # calculate the total area covered by the carpets
    total_area_carpets = num_carpets * area_carpet

    # calculate the total area of the floor that is uncovered
    area_uncovered = area_floor - total_area_carpets

    result = area_uncovered
    return result

print(solution())