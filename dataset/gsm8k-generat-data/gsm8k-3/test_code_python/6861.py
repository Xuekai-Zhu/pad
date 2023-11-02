def solution():
    """Ronald and his friend Max want to buy a new video game that was just released. The game costs $60. To earn money, they started selling ice cream in their yard, and they sell each ice cream for $5. How many ice creams will they need to sell for both to be able to afford to buy the game?"""
    # Define the cost of the video game and the price of an ice cream
    GAME_COST = 60
    ICE_CREAM_PRICE = 5

    # Calculate the amount of money needed to buy the game
    total_needed = GAME_COST

    # Calculate the amount of money they can earn from selling ice cream
    total_earned = 0
    ice_creams_sold = 0
    while total_earned < total_needed:
        total_earned += ICE_CREAM_PRICE
        ice_creams_sold += 1

    # Display the number of ice creams needed to buy the game
    result = ice_creams_sold
    return result

print(solution())