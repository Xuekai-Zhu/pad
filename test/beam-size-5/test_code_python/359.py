def solution():
    
    distance_to_friend = 200
    speed_to_friend = 70
    distance_to_detour = 10
    distance_to_route_home = 240
    speed_to_drive = 80
    distance_to_drive = distance_to_friend + distance_to_detour - distance_to_route_home
    time_to_drive = distance_to_drive / speed_to_drive
    result = time_to_drive
    return result

print(solution())