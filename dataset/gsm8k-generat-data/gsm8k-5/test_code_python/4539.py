def solution():
    two_bed_rooms = 8  # There are 8 rooms with two beds
    three_bed_rooms = 13 - two_bed_rooms  # There are 13 rooms in total, so the rest must have three beds
    total_beds = (two_bed_rooms * 2) + (three_bed_rooms * 3)  # Calculate the total number of beds
    result = total_beds
    return result

print(solution())