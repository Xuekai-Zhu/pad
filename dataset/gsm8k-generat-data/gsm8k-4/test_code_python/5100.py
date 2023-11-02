def solution():
    """The lights in Malcolm’s house are flickering, and he hopes that replacing all of his white lights with colored lights will make it stop. He buys 12 red lights, 3 times as many blue lights, and 6 green lights.  If he still has 5 colored lights left to buy, how many white lights did Malcolm have initially?"""
    # Define the number of red lights, blue lights, and green lights purchased
    red_lights = 12
    blue_lights = 3 * red_lights
    green_lights = 6

    # Calculate the total number of colored lights purchased
    colored_lights = red_lights + blue_lights + green_lights + 5

    # Calculate the initial number of white lights
    white_lights = colored_lights

    # Return the result
    result = white_lights
    return result

print(solution())