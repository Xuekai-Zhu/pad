def solution():
    """The lights in Malcolm’s house are flickering, and he hopes that replacing all of his white lights with colored lights will make it stop. He buys 12 red lights, 3 times as many blue lights, and 6 green lights. If he still has 5 colored lights left to buy, how many white lights did Malcolm have initially?"""
    red_lights = 12
    blue_lights = 3 * red_lights
    green_lights = 6
    total_colored_lights = red_lights + blue_lights + green_lights
    remaining_colored_lights = 5
    initial_white_lights = total_colored_lights + remaining_colored_lights
    result = initial_white_lights
    return result

print(solution())