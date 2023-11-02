def solution():
     rooms = 6
     living_room = 3
     other_rooms = rooms - living_room
     living_room_size = other_rooms * 3
     result = living_room_size
     return result

print(solution())