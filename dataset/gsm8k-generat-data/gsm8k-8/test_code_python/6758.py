def solution():
    # Define total walls and hours spent on one wall
    total_walls = 4
    hours_per_wall = 2

    # Calculate total hours spent on dining room
    dining_room_hours = hours_per_wall * 1

    # Calculate remaining walls to remove wallpaper from
    remaining_walls = total_walls - 1

    # Calculate total hours needed to remove wallpaper from remaining walls
    total_hours = remaining_walls * dining_room_hours
    result = total_hours
    return result

print(solution())