def solution():
    """Bucky earns money each weekend catching and selling fish. He wants to save up for a new video game, which costs $60. Last weekend he earned $35. He can earn $5 from trout and $4 from blue-gill. He caught five fish this Sunday. If 60% were trout, and the rest were blue-gill, how much more does he need to save before he can buy the game?"""
    # Define the cost of the video game and Bucky's earnings
    VIDEOGAME_COST = 60
    LAST_WEEK_EARNINGS = 35
    TROUT_EARNINGS = 5
    BLUEGILL_EARNINGS = 4

    # Determine the number of trout and bluegill caught
    trout_count = 5 * 0.6
    bluegill_count = 5 - trout_count

    # Calculate Bucky's earnings from this weekend's catch
    total_earnings = (trout_count * TROUT_EARNINGS) + (bluegill_count * BLUEGILL_EARNINGS)

    # Add last weekend's earnings to the total earnings
    total_earnings += LAST_WEEK_EARNINGS

    # Determine how much more Bucky needs to save for the video game
    savings_needed = VIDEOGAME_COST - total_earnings

    # Display how much more Bucky needs to save
    result = savings_needed
    return result

print(solution())