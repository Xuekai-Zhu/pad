def solution():
    
    two_bed_rooms = 8
    three_bed_rooms = 13 - two_bed_rooms
    total_beds = (2 * two_bed_rooms) + (3 * three_bed_rooms)
    result = total_beds
    return result

print(solution())