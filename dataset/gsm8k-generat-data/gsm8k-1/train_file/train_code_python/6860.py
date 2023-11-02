def solution():
    """Ronald and his friend Max want to buy a new video game that was just released. The game costs $60. To earn money,
    they started selling ice cream in their yard, and they sell each ice cream for $5. How many ice creams will they need
    to sell for both to be able to afford to buy the game?"""
    game_price = 60
    ice_cream_price = 5
    total_earnings = game_price
    ice_creams_needed = 0
    while total_earnings > 0:
        total_earnings -= ice_cream_price
        ice_creams_needed += 1
    result = ice_creams_needed
    return result

print(solution())