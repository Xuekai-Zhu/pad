def solution():
    """At Palm Meadows, there are 13 hotel rooms. Eight of the rooms have two beds in them and the rest have three beds. How many beds are there in total?"""
    two_bed_rooms = 8
    three_bed_rooms = 13 - two_bed_rooms
    total_beds = (2 * two_bed_rooms) + (3 * three_bed_rooms)
    result = total_beds
    return result

print(solution())