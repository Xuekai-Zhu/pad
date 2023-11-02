def solution():
    surfboard_length = 7  # Austin's surfboard is 7 feet long
    shortest_wave = surfboard_length + 3  # The shortest wave was 3 feet higher than the surfboard length
    austin_height = (shortest_wave - 4) / 4  # Solve equation for Austin's height
    highest_wave = 4 * austin_height + 2  # Calculate the height of the highest wave Austin caught
    result = highest_wave
    return result

print(solution())