def solution():
    """In a school garden, there are flowers in different colors. In total there are 96 flowers of four colors: green, red, blue, and yellow. There are 9 green flowers and three times more red flowers. Blue flowers make up to 50% of the total flower count. How many yellow flowers are there?"""
    total_flowers = 96
    green_flowers = 9
    red_flowers = 3 * green_flowers
    blue_flowers = total_flowers * 0.5
    yellow_flowers = total_flowers - green_flowers - red_flowers - blue_flowers
    result = yellow_flowers
    return result

print(solution())