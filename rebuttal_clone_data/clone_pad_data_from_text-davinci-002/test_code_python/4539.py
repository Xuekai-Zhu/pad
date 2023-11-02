def solution():
    two_bed_rooms = 8
    three_bed_rooms = 5
    two_beds_per_room = 2
    three_beds_per_room = 3
    total_beds = (two_bed_rooms * two_beds_per_room) + (three_bed_rooms * three_beds_per_room)
    result = total_beds
    return result

print(solution())