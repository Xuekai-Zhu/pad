def solution():
    """Ned is an explosives specialist racing to deactivate a time bomb on the top floor of a building. The building has twenty flights of stairs to the top floor, and Ned can run up one flight of stairs in eleven seconds. The time bomb has 72 seconds left on the timer, and Ned has spent 165 seconds running up the stairs. How many seconds will Ned have to diffuse the bomb when he reaches it?"""
    stairs_per_floor = 1
    floors = 20
    seconds_per_stair = 11
    total_seconds_running = seconds_per_stair * stairs_per_floor * floors
    seconds_left = 72 - (total_seconds_running - 165)
    result = seconds_left
    return result

print(solution())