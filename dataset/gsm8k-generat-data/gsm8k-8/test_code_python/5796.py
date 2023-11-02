def solution():
    # Calculate the area of the entire garden
    garden_area = 220 * 120

    # Calculate the area of the tilled land (which is half of the entire garden)
    tilled_land_area = garden_area / 2

    # Calculate the area of the portion that won't have trellises (which is 2/3 of the remaining area)
    non_trellis_area = (garden_area - tilled_land_area) * (2 / 3)

    # Calculate the area of the raised beds (which is the remaining area)
    raised_bed_area = garden_area - tilled_land_area - non_trellis_area

    result = raised_bed_area
    return result

print(solution())