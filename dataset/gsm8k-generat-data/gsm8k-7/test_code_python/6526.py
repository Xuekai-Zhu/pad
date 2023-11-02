def solution():
    initial_cost = 200
    value_after_triple = initial_cost * 3
    sold_percentage = 0.4
    
    # Calculate the total value of the games after they triple in value
    total_value = value_after_triple
    
    # Calculate the amount of games Tom sold
    num_games_sold = total_value * sold_percentage
    
    # Calculate the price Tom sold the games for
    price_per_game = total_value / (initial_cost * 3)
    total_sale_price = num_games_sold * price_per_game
    
    result = total_sale_price
    return result

print(solution())