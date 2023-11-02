def solution():
    inches_in_foot = 12
    feet_in_room = 10
    room_area = feet_in_room ** 2
    inches_in_room = room_area * inches_in_foot ** 2
    result = inches_in_room
    return result

print(solution())