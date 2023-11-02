def solution():
    # Calculate the total time Eric spent removing wallpaper from one wall
    time_per_wall = 2  # Eric spent 2 hours removing wallpaper from one wall
    total_time = time_per_wall * 4  # Eric has 4 walls in his dining room

    # Calculate the time Eric needs to remove wallpaper from his living room
    living_room_walls = 4  # Eric has 4 walls in his living room
    time_for_living_room = living_room_walls * time_per_wall

    # Calculate the remaining time Eric needs to remove wallpaper
    remaining_time = total_time + time_for_living_room - total_time
    result = remaining_time
    return result

print(solution())