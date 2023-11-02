def solution():
    """Mark builds an apartment that is 16 by 10 feet. There are 6 rooms in total. All the rooms are the same size except the living room which is as big as 3 other rooms. How big is the living room?"""
    apartment_area = 16 * 10
    num_rooms = 6
    equal_rooms_area = apartment_area / num_rooms
    living_room_area = equal_rooms_area * 3
    result = living_room_area
    return result

print(solution())