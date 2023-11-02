def solution():
    time_to_gate = 15
    time_to_building = 6
    time_allowed = 30
    time_to_room = time_allowed - time_to_gate - time_to_building
    result = time_to_room
    return result

print(solution())