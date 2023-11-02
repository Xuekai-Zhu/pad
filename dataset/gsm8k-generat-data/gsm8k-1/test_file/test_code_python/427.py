def solution():
    """Dora wants to buy a skipping rope that costs $6, a board game that costs $11, and a playground ball that costs $2. She has saved $2 from her allowance, and her mother gave her $16. How much more money does Dora need to buy the skipping rope, the game, and the ball?"""
    skipping_rope_cost = 6
    board_game_cost = 11
    playground_ball_cost = 2
    total_cost = skipping_rope_cost + board_game_cost + playground_ball_cost
    total_saved = 2 + 16
    money_needed = total_cost - total_saved
    result = money_needed
    return result

print(solution())