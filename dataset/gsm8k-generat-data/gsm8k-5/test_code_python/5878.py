def solution():
    # Calculate the total width of splashes from pebbles
    pebbles_splash_width = 1/4
    total_pebbles_splash_width = pebbles_splash_width * 6

    # Calculate the total width of splashes from rocks
    rocks_splash_width = 1/2
    total_rocks_splash_width = rocks_splash_width * 3

    # Calculate the total width of splashes from boulders
    boulders_splash_width = 2
    total_boulders_splash_width = boulders_splash_width * 2

    # Calculate the total width of all the splashes
    total_splash_width = total_pebbles_splash_width + total_rocks_splash_width + total_boulders_splash_width
    result = total_splash_width
    return result

print(solution())