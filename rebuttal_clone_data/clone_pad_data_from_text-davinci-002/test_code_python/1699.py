def solution():
    red_flowers = 2 * orange_flowers
    yellow_flowers = red_flowers - 5
    pink_and_purple_flowers = ((red_flowers + orange_flowers + yellow_flowers) - 10) / 2
    result = pink_and_purple_flowers
    return result

print(solution())