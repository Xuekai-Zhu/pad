def solution():
    """Maddie bought 2 packs of white T-shirts and 4 packs of blue T-shirts for her basketball team. The white T-shirts come in packs of 5, and the blue T-shirts come in packs of 3. Each T-shirt cost $3. How much did Maddie spend in all?"""
    # Define the number of packs of white and blue t-shirts
    white_packs = 2
    blue_packs = 4

    # Define the number of t-shirts per pack
    white_per_pack = 5
    blue_per_pack = 3

    # Define the cost per t-shirt
    cost_per_shirt = 3

    # Calculate the total number of t-shirts
    total_white = white_packs * white_per_pack
    total_blue = blue_packs * blue_per_pack
    total_shirts = total_white + total_blue

    # Calculate the total cost
    total_cost = total_shirts * cost_per_shirt

    result = total_cost
    return result

print(solution())