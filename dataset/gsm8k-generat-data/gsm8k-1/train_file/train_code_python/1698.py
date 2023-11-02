def solution():
    """A garden is filled with 105 flowers of various colors. There are twice as many red flowers as orange. There are five fewer yellow flowers than red. If there are 10 orange flowers, how many pink and purple flowers are there if they have the same amount and there are no other colors?"""
    orange_flowers = 10
    red_flowers = 2 * orange_flowers
    yellow_flowers = red_flowers - 5
    total_flowers = 105
    pink_purple_flowers = (total_flowers - orange_flowers - red_flowers - yellow_flowers) / 2
    result = pink_purple_flowers
    return result

print(solution())