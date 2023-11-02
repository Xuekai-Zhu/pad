def solution():
    game_cost = 60  # The video game costs $60
    money_earned_per_ice_cream = 5  # They earn $5 for each ice cream sold

    # Calculate the total amount of money needed to buy the game
    total_money_needed = game_cost * 2  # Both Ronald and Max need to contribute

    # Calculate how many ice creams they need to sell to earn enough money
    ice_creams_needed = total_money_needed / money_earned_per_ice_cream

    result = ice_creams_needed
    return result

print(solution())