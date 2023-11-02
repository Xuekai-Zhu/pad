def solution():
    """At Palm Meadows, there are 13 hotel rooms. Eight of the rooms have two beds in them and the rest have three beds. How many beds are there in total?"""
    num_two_bed_rooms = 8
    num_three_bed_rooms = 13 - num_two_bed_rooms
    total_beds = (num_two_bed_rooms * 2) + (num_three_bed_rooms * 3)
    result = total_beds
    return result

print(solution())