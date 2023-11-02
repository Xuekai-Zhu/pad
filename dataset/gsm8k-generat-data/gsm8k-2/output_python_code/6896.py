def solution():
    """Mike gets paid 100 dollars a week. He decides to spend half of that at an arcade. He spends 10 dollars at the arcade on food and uses the rest on arcade tokens. He can play for 1 hour for $8. How many minutes can he play?"""
    weekly_pay = 100
    arcade_spending = weekly_pay / 2
    tokens_spending = arcade_spending - 10
    token_price = 8 / 60
    total_playing_time = tokens_spending / token_price
    result = total_playing_time
    return result

print(solution())