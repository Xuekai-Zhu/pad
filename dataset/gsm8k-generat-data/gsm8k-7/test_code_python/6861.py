def solution():
    game_cost = 60
    ice_cream_price = 5

    # Calculate the total amount of money they need
    total_money_needed = game_cost

    # Calculate how much money they can earn per ice cream sold
    money_per_ice_cream = ice_cream_price

    # Calculate how many ice creams they need to sell to afford the game
    num_ice_creams_needed = total_money_needed / money_per_ice_cream
    result = int(num_ice_creams_needed)  # round down to nearest integer
    return result

print(solution())