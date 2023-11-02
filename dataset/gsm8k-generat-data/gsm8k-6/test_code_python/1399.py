def solution():
    # Calculate Austin's height
    surfboard_length = 7
    shortest_wave = surfboard_length + 3
    height = shortest_wave - 4
    # Calculate the height of the highest wave
    highest_wave = 4 * height + 2
    result = highest_wave
    return result

print(solution())