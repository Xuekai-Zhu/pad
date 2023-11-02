def solution():
    """Eric spent 2 hours removing wallpaper from just 1 wall of his 4 walled dining room.  He also needs to remove wallpaper from his 4 walled living room.  How many hours will it take him to remove the remaining wallpaper?"""
    # Define the number of walls in the dining and living rooms
    dining_walls = 4
    living_walls = 4

    # Define the time it takes Eric to remove wallpaper from one wall
    time_per_wall = 2

    # Calculate the total time it takes Eric to remove wallpaper from the dining room
    dining_time = dining_walls * time_per_wall

    # Calculate the remaining time it will take Eric to remove wallpaper from the living room
    living_time = living_walls * time_per_wall - dining_time

    # Display the remaining time
    result = living_time
    return result

print(solution())