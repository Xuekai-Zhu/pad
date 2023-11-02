def solution():
    pebble_splash = 0.25
    rock_splash = 0.5
    boulder_splash = 2.0

    num_pebbles = 6
    num_rocks = 3
    num_boulders = 2

    # Calculate the total width of the splashes for all pebbles
    total_pebble_splash = num_pebbles * pebble_splash

    # Calculate the total width of the splashes for all rocks
    total_rock_splash = num_rocks * rock_splash

    # Calculate the total width of the splashes for all boulders
    total_boulder_splash = num_boulders * boulder_splash

    # Calculate the total width of all splashes
    total_splash_width = total_pebble_splash + total_rock_splash + total_boulder_splash
    result = total_splash_width
    return result

print(solution())