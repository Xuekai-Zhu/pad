def solution():
    """Linda is building a new hotel with two wings. The first wing has 9 floors and each floor has 6 halls each with 32 rooms. The second wing has 7 floors each with 9 halls with 40 rooms each. How many rooms are in the hotel total?"""
    first_wing_floors = 9
    first_wing_halls = 6
    first_wing_rooms = 32
    second_wing_floors = 7
    second_wing_halls = 9
    second_wing_rooms = 40
    
    first_wing_total_rooms = first_wing_floors * first_wing_halls * first_wing_rooms
    second_wing_total_rooms = second_wing_floors * second_wing_halls * second_wing_rooms
    
    total_rooms = first_wing_total_rooms + second_wing_total_rooms
    
    result = total_rooms
    
    return result

print(solution())