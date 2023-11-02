def solution():
    
    # Define the prices of each item
    skipping_rope_price = 6
    board_game_price = 11
    playground_ball_price = 2

    # Define the amount of money Dora has saved
    savings = 2

    # Define the amount of money Dora's mother gave her
    mother_money = 16

    # Calculate the total cost of the skipping rope, board game, and playground ball
    total_cost = skipping_rope_price + board_game_price + playground_ball_price

    # Calculate the remaining amount of money Dora needs to buy the skipping rope, board game, and playground ball
    remaining_money = total_cost - savings - mother_money

    # Display the remaining amount of money Dora needs to buy the skipping rope, board game, and playground ball
    result = remaining_money
    return result

print(solution())