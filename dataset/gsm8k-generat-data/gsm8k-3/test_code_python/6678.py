def solution():
    """A citrus grove has laid out their plans for their sixteen orchards for the growing season. Lemons, their most popular citrus fruit, will take up eight orchards. Oranges are their second most popular fruit and will occupy half as many orchards as the lemons. Limes and grapefruits will split the remaining orchards. How many citrus orchards will be growing grapefruits?"""
    # Define the number of orchards for lemons and oranges
    lemon_orchards = 8
    orange_orchards = lemon_orchards // 2

    # Calculate the number of orchards for limes and grapefruits
    lime_grapefruit_orchards = 16 - lemon_orchards - orange_orchards

    # Calculate the number of orchards for grapefruits
    grapefruit_orchards = lime_grapefruit_orchards // 2

    # Display the number of citrus orchards growing grapefruits
    result = grapefruit_orchards
    return result

print(solution())