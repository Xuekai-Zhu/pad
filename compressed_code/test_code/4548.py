def solution():
    
    pebble_splash = 1/4
    rock_splash = 1/2
    boulder_splash = 2
    total_splash = (pebble_splash * 6) + (rock_splash * 3) + (boulder_splash * 2)
    result = total_splash
    return result

print(solution())