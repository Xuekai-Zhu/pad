def solution():
    """Ronald and his friend Max want to buy a new video game that was just released. The game costs $60. To earn money, they started selling ice cream in their yard, and they sell each ice cream for $5. How many ice creams will they need to sell for both to be able to afford to buy the game?"""
    # Define the cost of the video game
    game_cost = 60

    # Define the price of each ice cream
    ice_cream_price = 5

    # Calculate the total amount of money they need to make to afford the game
    total_money_needed = game_cost

    # Calculate the number of ice creams they need to sell
    ice_creams_needed = total_money_needed / ice_cream_price

    # Round up to the nearest whole number
    ice_creams_needed = math.ceil(ice_creams_needed)

    # Return the result
    result = ice_creams_needed
    return result

print(solution())