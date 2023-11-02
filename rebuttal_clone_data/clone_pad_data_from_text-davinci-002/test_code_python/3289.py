def solution():
     first_wing_floors = 9
     first_wing_halls = 6
     first_wing_rooms = 32
     second_wing_floors = 7
     second_wing_halls = 9
     second_wing_rooms = 40
     total_rooms = (first_wing_floors * first_wing_halls * first_wing_rooms) + (second_wing_floors * second_wing_halls * second_wing_rooms)
     result = total_rooms
     return result

print(solution())