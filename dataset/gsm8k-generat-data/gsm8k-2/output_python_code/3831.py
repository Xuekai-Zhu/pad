def solution():
    """A florist is making bouquets for the weekend. The florist uses red, yellow, orange, and purple flowers, and each bouquet contains 9 flowers of any color combinations. This week he planted 125 seeds for each color of flower. Unfortunately, a fungus killed 45 red flowers, 61 yellow, 30 orange, and 40 purple flowers. How many bouquets can the florist make this weekend?"""
    flowers_per_color = 125
    total_flowers = (flowers_per_color - 45) + (flowers_per_color - 61) + (flowers_per_color - 30) + (flowers_per_color - 40)
    bouquets = total_flowers // 9
    result = bouquets
    return result

print(solution())