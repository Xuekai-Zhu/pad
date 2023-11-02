def solution():
    # Calculate the number of blue lights Malcolm buys
    blue_lights = 3 * 12

    # Calculate the total number of colored lights Malcolm buys
    colored_lights = 12 + blue_lights + 6 + 5

    # Calculate the number of white lights Malcolm had initially
    initial_lights = colored_lights + 5
    result = initial_lights
    return result

print(solution())