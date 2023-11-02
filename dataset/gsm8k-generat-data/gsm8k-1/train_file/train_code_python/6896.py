def solution():
    """Mike gets paid 100 dollars a week. He decides to spend half of that at an arcade. He spends 10 dollars at the arcade on food and uses the rest on arcade tokens. He can play for 1 hour for $8. How many minutes can he play?"""
    weekly_pay = 100
    arcade_spending = weekly_pay / 2
    food_spending = 10
    token_spending = arcade_spending - food_spending
    play_time_per_token = 60 # minutes
    cost_per_token = 8
    tokens_played = token_spending / cost_per_token
    total_play_time = tokens_played * play_time_per_token
    result = total_play_time
    
    return result

print(solution())