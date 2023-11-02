def solution():
    """Nick is trying to raise money for a charity. He is selling candy bars for $5. He is also selling chocolate oranges for $10. He wants to raise $1000. He only had 20 chocolate oranges that he sold out. How many candy bars does Nick need to sell to reach his goal?"""
    chocolate_oranges_sold = 20
    chocolate_oranges_profit = chocolate_oranges_sold * 10
    remaining_goal = 1000 - chocolate_oranges_profit
    candy_bars_price = 5
    candy_bars_needed = remaining_goal / candy_bars_price
    result = candy_bars_needed
    return result

print(solution())