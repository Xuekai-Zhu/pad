def solution():
    # Calculate the area of the whole plot
    total_area = 200 * 50

    # Calculate the area of the sidewalk
    sidewalk_area = 3 * 50

    # Calculate the area of the flower beds
    flower_bed1_area = 4 * 25
    flower_bed2_area = 4 * 25
    flower_bed3_area = 10 * 12
    flower_bed4_area = 7 * 8
    flower_beds_area = flower_bed1_area + flower_bed2_area + flower_bed3_area + flower_bed4_area

    # Calculate the area of the yard minus the sidewalk and flower beds
    yard_area = total_area - sidewalk_area - flower_beds_area
    result = yard_area
    return result

print(solution())