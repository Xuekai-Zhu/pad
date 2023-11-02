def solution():
    # Define the width of each type of splash
    pebble_splash = 1/4
    rock_splash = 1/2
    boulder_splash = 2

    # Calculate the total width of the splashes
    total_splash_width = 6*pebble_splash + 3*rock_splash + 2*boulder_splash
    result = total_splash_width
    return result

print(solution())