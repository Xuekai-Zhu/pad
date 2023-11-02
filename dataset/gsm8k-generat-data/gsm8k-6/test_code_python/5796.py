def solution():
    # Calculate the size of the tilled land
    tilled_land = (1/2) * 220 * 120

    # Calculate the size of the part with trellises
    trellis_land = (1/3) * (220 * 120 - tilled_land)

    # Calculate the size of the raised bed section
    raised_bed_land = 220 * 120 - tilled_land - trellis_land

    result = raised_bed_land
    return result

print(solution())