def solution():
    """TreQuan is throwing rocks in the river and he notices that the bigger the rock, the wider the splash. Pebbles make a splash that is a 1/4 meter wide. Rocks make a splash that is 1/2 a meter wide, and boulders create a splash that is 2 meters wide. If he tosses 6 pebbles, 3 rocks, and 2 boulders, what is the total width of the splashes he makes?"""
    pebble_splash = 1/4
    rock_splash = 1/2
    boulder_splash = 2
    num_pebbles = 6
    num_rocks = 3
    num_boulders = 2
    total_splash_width = (pebble_splash * num_pebbles) + (rock_splash * num_rocks) + (boulder_splash * num_boulders)
    result = total_splash_width
    return result

print(solution())