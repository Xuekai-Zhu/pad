def solution():
    """A citrus grove has laid out their plans for their sixteen orchards for the growing season. Lemons, their most popular citrus fruit, will take up eight orchards. Oranges are their second most popular fruit and will occupy half as many orchards as the lemons. Limes and grapefruits will split the remaining orchards. How many citrus orchards will be growing grapefruits?"""
    total_orchards = 16
    lemon_orchards = 8
    orange_orchards = lemon_orchards / 2
    lime_orchards = (total_orchards - lemon_orchards - orange_orchards) / 2
    grapefruit_orchards = lime_orchards
    result = grapefruit_orchards
    return result

print(solution())