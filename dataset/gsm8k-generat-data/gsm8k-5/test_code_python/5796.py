def solution():
    # Calculate the area of the whole garden
    whole_garden = 220 * 120

    # Calculate the area of the tilled land
    tilled_land = whole_garden / 2

    # Calculate the area not taken up by tilled land
    remaining_area = whole_garden - tilled_land

    # Calculate the area for trellises
    trellis_area = remaining_area / 3

    # Calculate the area for raised beds
    raised_bed_area = remaining_area - trellis_area

    result = raised_bed_area
    return result

print(solution())