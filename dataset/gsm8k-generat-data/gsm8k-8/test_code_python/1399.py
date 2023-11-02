def solution():
    # Define the variables
    surfboard_length = 7
    shortest_wave_height = surfboard_length + 3
    height = shortest_wave_height - 4
    highest_wave_height = 2 + 4*height

    result = highest_wave_height
    return result

print(solution())