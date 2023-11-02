def solution():
    # Calculate the area of the whole yard
    whole_yard = 200 * 50  # plot of land is 200 feet wide by 50 feet

    # Calculate the area of the sidewalk
    sidewalk = 3 * 50  # sidewalk is 3 feet wide by 50 feet long

    # Calculate the area of the flower beds
    flower_bed_1 = 4 * 25  # first flower bed is 4 feet deep by 25 feet long
    flower_bed_2 = 4 * 25  # second flower bed is 4 feet deep by 25 feet long
    flower_bed_3 = 10 * 12  # third flower bed is 10 feet by 12 feet
    flower_bed_4 = 7 * 8  # fourth flower bed is 7 feet by 8 feet
    total_flower_beds = flower_bed_1 + flower_bed_2 + flower_bed_3 + flower_bed_4

    # Calculate the area of the yard minus the sidewalk and flower beds
    area_yard = whole_yard - (sidewalk + total_flower_beds)
    result = area_yard
    return result

print(solution())