def solution():
    """Mark builds an apartment that is 16 by 10 feet. There are 6 rooms in total. All the rooms are the same size except the living room which is as big as 3 other rooms. How big is the living room?"""
    total_area = 16 * 10  # total area of the apartment
    living_room_area = total_area / (6/4 + 1)  # dividing the total area by the number of equal rooms plus the living room
    result = living_room_area
    return result

print(solution())