def solution():
    toys_time = 5  # Time to pick up toys
    vacuum_time = 20  # Time to vacuum
    windows_time = 15  # Time to clean windows
    dusting_time = 10  # Time to dust furniture
    weeks = 4  # Kitty has been cleaning for 4 weeks

    # Calculate the total time Kitty spent cleaning the living room
    living_room_time = (toys_time + vacuum_time + windows_time + dusting_time) * weeks

    result = living_room_time
    return result

print(solution())