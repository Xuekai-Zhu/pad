def solution():
    """A florist is making bouquets for the weekend. The florist uses red, yellow, orange, and purple flowers, and each bouquet contains 9 flowers of any color combinations. This week he planted 125 seeds for each color of flower. Unfortunately, a fungus killed 45 red flowers, 61 yellow, 30 orange, and 40 purple flowers. How many bouquets can the florist make this weekend?"""
    flowers_planted = 125
    flowers_killed = {"red": 45, "yellow": 61, "orange": 30, "purple": 40}
    total_flowers = sum([flowers_planted - flowers_killed[color] for color in flowers_killed])
    bouquets_per_flower = total_flowers // 9
    result = bouquets_per_flower
    return result

print(solution())