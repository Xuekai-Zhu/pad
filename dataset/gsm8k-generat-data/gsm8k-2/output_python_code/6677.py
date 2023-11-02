def solution():
    """A citrus grove has laid out their plans for their sixteen orchards for the growing season. Lemons, their most popular citrus fruit, will take up eight orchards. Oranges are their second most popular fruit and will occupy half as many orchards as the lemons. Limes and grapefruits will split the remaining orchards. How many citrus orchards will be growing grapefruits?"""
    lemon_orchards = 8
    orange_orchards = lemon_orchards / 2
    remaining_orchards = 16 - lemon_orchards - orange_orchards
    grapefruit_orchards = remaining_orchards / 2
    result = grapefruit_orchards
    return result

print(solution())