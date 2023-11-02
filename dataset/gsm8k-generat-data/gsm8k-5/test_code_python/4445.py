def solution():
    # Square footage of living room walls
    living_room_area = 4 * 40 * 10  # 4 walls, each 40 feet by 10 feet

    # Square footage of bedroom walls
    bedroom_area = 2 * (10 * 10) + 2 * (12 * 10)  # 2 walls, each 10 feet by 10 feet, and 2 walls, each 12 feet by 10 feet

    # Total square footage of walls to be painted
    total_area = living_room_area + bedroom_area
    result = total_area
    return result

print(solution())