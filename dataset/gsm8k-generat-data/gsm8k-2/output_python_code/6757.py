def solution():
    """Eric spent 2 hours removing wallpaper from just 1 wall of his 4 walled dining room. He also needs to remove wallpaper from his 4 walled living room. How many hours will it take him to remove the remaining wallpaper?"""
    dining_room_walls = 4
    living_room_walls = 4
    time_per_wall = 2
    total_time = time_per_wall * (dining_room_walls + living_room_walls - 1)
    result = total_time
    return result

print(solution())