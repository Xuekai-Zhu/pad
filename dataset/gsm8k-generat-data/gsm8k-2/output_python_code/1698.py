def solution():
    """A garden is filled with 105 flowers of various colors. There are twice as many red flowers as orange. There are five fewer yellow flowers than red. If there are 10 orange flowers, how many pink and purple flowers are there if they have the same amount and there are no other colors?"""
    orange_flowers = 10
    red_flowers = 2 * orange_flowers
    yellow_flowers = red_flowers - 5
    total_known_flowers = orange_flowers + red_flowers + yellow_flowers
    pink_and_purple = 105 - total_known_flowers
    pink_flowers = pink_and_purple / 2
    purple_flowers = pink_and_purple / 2
    result = pink_flowers + purple_flowers
    return result

print(solution())