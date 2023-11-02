def solution():
    
    weekly_pay = 100
    arcade_spending = weekly_pay / 2
    tokens_spending = arcade_spending - 10
    token_price = 8 / 60
    total_playing_time = tokens_spending / token_price
    result = total_playing_time
    return result

print(solution())