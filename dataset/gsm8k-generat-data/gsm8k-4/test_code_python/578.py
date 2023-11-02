def solution():
    """Bucky earns money each weekend catching and selling fish. He wants to save up for a new video game, which costs $60. Last weekend he earned $35. He can earn $5 from trout and $4 from blue-gill. He caught five fish this Sunday. If 60% were trout, and the rest were blue-gill, how much more does he need to save before he can buy the game?"""
    
    # Define the cost of the video game and the money earned last weekend
    GAME_COST = 60
    EARNED_LAST_WEEKEND = 35
    
    # Define the amount earned per fish and the number of fish caught
    TROUT_EARNINGS = 5
    BLUEGILL_EARNINGS = 4
    FISH_CAUGHT = 5
    
    # Calculate the earnings from each type of fish caught
    trout_caught = 0.6 * FISH_CAUGHT
    bluegill_caught = FISH_CAUGHT - trout_caught
    earnings_from_trout = trout_caught * TROUT_EARNINGS
    earnings_from_bluegill = bluegill_caught * BLUEGILL_EARNINGS
    
    # Calculate the total earnings from catching fish this weekend
    total_earnings = earnings_from_trout + earnings_from_bluegill
    
    # Calculate the total amount saved so far
    total_saved = EARNED_LAST_WEEKEND + total_earnings
    
    # Calculate the amount still needed to buy the game
    amount_needed = GAME_COST - total_saved
    
    # Return the result
    result = amount_needed
    return result

print(solution())