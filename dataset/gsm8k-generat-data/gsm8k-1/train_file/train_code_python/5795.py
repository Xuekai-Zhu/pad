def solution():
    """Bob is building a vegetable garden. It is 220 feet long by 120 feet wide. Half of the garden is going to be tilled land. A third of the rest of it will have trellises for vining plants, and the rest will be devoted to raised beds. How big will the raised bed section of the garden be?"""
    length = 220
    width = 120
    total_area = length * width
    tilled_land = total_area / 2
    remaining_area = total_area - tilled_land
    trellis_area = remaining_area / 3
    raised_bed_area = remaining_area - trellis_area
    result = raised_bed_area
    return result

print(solution())