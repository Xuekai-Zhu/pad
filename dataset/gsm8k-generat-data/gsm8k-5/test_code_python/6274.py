def solution():
    # Calculate the total area of the front yard
    total_area = 200 * 50

    # Calculate the area of the sidewalk
    sidewalk_area = 3 * 50

    # Calculate the area of the flower beds
    flower_bed_1 = 4 * 25
    flower_bed_2 = 4 * 25
    flower_bed_3 = 10 * 12
    flower_bed_4 = 7 * 8
    flower_beds_area = flower_bed_1 + flower_bed_2 + flower_bed_3 + flower_bed_4

    # Calculate the area of sod needed to cover the yard, minus the sidewalk and flower beds
    sod_area = total_area - sidewalk_area - flower_beds_area
    result = sod_area
    return result

print(solution())