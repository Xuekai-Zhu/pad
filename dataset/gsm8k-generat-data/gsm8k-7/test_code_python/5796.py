def solution():
    length = 220
    width = 120

    # Calculate the area of the entire garden
    total_area = length * width

    # Calculate the area of the tilled land
    tilled_area = total_area / 2

    # Calculate the area remaining after tilled land
    remaining_area = total_area - tilled_area

    # Calculate the area for trellises
    trellis_area = remaining_area / 3

    # Calculate the area for raised beds
    raised_bed_area = remaining_area - trellis_area

    result = raised_bed_area
    return result

print(solution())