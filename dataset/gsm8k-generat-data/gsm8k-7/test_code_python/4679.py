def solution():
    total_turtles = 42
    wave_swept = total_turtles / 3

    # Calculate the number of turtles still on the sand
    still_on_sand = total_turtles - wave_swept
    result = still_on_sand
    return result

print(solution())