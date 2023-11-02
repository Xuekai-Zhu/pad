def solution():
    # Calculate the total width of the splashes from TreQuan's rocks
    pebble_splash = 0.25 * 6  # each pebble creates a 1/4 meter wide splash
    rock_splash = 0.5 * 3  # each rock creates a 1/2 meter wide splash
    boulder_splash = 2 * 2  # each boulder creates a 2 meter wide splash
    total_splash = pebble_splash + rock_splash + boulder_splash
    result = total_splash
    return result

print(solution())