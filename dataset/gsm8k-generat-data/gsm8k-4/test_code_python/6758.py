def solution():
    """Eric spent 2 hours removing wallpaper from just 1 wall of his 4 walled dining room. He also needs to remove wallpaper from his 4 walled living room. How many hours will it take him to remove the remaining wallpaper?"""
    # Define the number of walls in each room
    dining_room_walls = 4
    living_room_walls = 4

    # Define the time it takes to remove wallpaper from one wall
    time_per_wall = 2

    # Calculate the total time spent on the dining room walls
    dining_room_time = time_per_wall * (dining_room_walls - 1)

    # Calculate the total time needed to remove the wallpaper in both rooms
    total_time = dining_room_time + (living_room_walls * time_per_wall)

    result = total_time
    return result

print(solution())