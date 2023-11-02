def solution():
    # Calculate the total number of colored lights Malcolm bought
    total_colored_lights = 12 + 3*12 + 6  # Malcolm bought 12 red, 3 times as many blue, and 6 green lights

    # Calculate the number of white lights Malcolm initially had
    initial_white_lights = total_colored_lights + 5  # Malcolm still has 5 colored lights left to buy
    result = initial_white_lights
    return result

print(solution())