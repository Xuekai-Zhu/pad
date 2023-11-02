def solution():
    # Calculate the area of one side of the roof
    area_one_side = 20 * 40 / 2  # two slanted rectangular sides measuring 20 feet by 40 feet

    # Calculate the total area of all three roofs
    total_area = area_one_side * 3

    # Calculate the number of shingles needed to cover the total area
    shingles_needed = total_area * 8  # 8 shingles to cover one square foot of roof

    result = shingles_needed
    return result

print(solution())