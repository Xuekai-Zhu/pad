def solution():
    """Ronald and his friend Max want to buy a new video game that was just released. The game costs $60. To earn money, they started selling ice cream in their yard, and they sell each ice cream for $5. How many ice creams will they need to sell for both to be able to afford to buy the game?"""
    game_cost = 60
    ice_cream_price = 5
    total_money_needed = game_cost
    total_money_earned = 0
    ice_creams_sold = 0
    while total_money_earned < total_money_needed:
        total_money_earned += ice_cream_price
        ice_creams_sold += 1

    result = ice_creams_sold
    return result

print(solution())