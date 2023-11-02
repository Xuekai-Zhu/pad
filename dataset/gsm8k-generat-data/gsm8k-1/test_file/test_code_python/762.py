def solution():
    """Marissa bought a ball at the store for $20. If she had $80 on her and used the rest of the money to buy her brother Jimmy, candy bars sold at $5 each, how many candy bars did Marissa buy for Jimmy?"""
    ball_cost = 20
    total_money = 80
    candy_bar_cost = 5
    money_left = total_money - ball_cost
    candy_bars_bought = int(money_left / candy_bar_cost)
    result = candy_bars_bought
    return result

print(solution())