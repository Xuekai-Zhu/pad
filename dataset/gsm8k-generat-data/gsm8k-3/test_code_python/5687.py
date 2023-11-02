def solution():
    """Maddie bought 2 packs of white T-shirts and 4 packs of blue T-shirts for her basketball team. The white T-shirts come in packs of 5, and the blue T-shirts come in packs of 3. Each T-shirt cost $3. How much did Maddie spend in all?"""
    # Define the number of T-shirts in each pack and the cost per T-shirt
    WHITE_SHIRTS_PER_PACK = 5
    BLUE_SHIRTS_PER_PACK = 3
    SHIRT_COST = 3

    # Define the number of packs of each color purchased
    white_packs = 2
    blue_packs = 4

    # Calculate the total number of white and blue T-shirts purchased
    total_white_shirts = white_packs * WHITE_SHIRTS_PER_PACK
    total_blue_shirts = blue_packs * BLUE_SHIRTS_PER_PACK

    # Calculate the total cost of all the T-shirts
    total_cost = SHIRT_COST * (total_white_shirts + total_blue_shirts)

    # Display the total cost
    result = total_cost
    return result

print(solution())