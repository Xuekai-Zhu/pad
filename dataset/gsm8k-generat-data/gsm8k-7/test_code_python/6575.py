def solution():
    bed_height = 2  # in feet
    bed_width = 2  # in feet
    bed_length = 8  # in feet
    plank_width = 1  # in feet
    num_beds = 10

    # Calculate the length of each side plank needed per bed
    side_plank_length = (bed_height + bed_width) * 2

    # Calculate the length of the long plank needed per bed
    long_plank_length = bed_length + (2 * plank_width)

    # Calculate the total length of planks needed for one bed
    total_bed_plank_length = (2 * side_plank_length) + long_plank_length

    # Calculate the total length of planks needed for all beds
    total_plank_length = total_bed_plank_length * num_beds

    # Calculate the number of 8-foot long planks needed
    num_eight_foot_planks = total_plank_length / 8

    result = num_eight_foot_planks
    return result

print(solution())