def solution():
    
    total_area = 220 * 120
    tilled_area = total_area / 2
    remaining_area = total_area - tilled_area
    trellis_area = remaining_area / 3
    raised_bed_area = remaining_area - trellis_area
    result = raised_bed_area
    return result

print(solution())