def solution():
    """Nick is trying to raise money for a charity. He is selling candy bars for $5. He is also selling chocolate oranges for $10. He wants to raise $1000. He only had 20 chocolate oranges that he sold out. How many candy bars does Nick need to sell to reach his goal?"""
    candy_price = 5
    orange_price = 10
    orange_count = 20
    goal = 1000
    orange_sales = orange_price * orange_count
    remaining_goal = goal - orange_sales
    candy_count = remaining_goal // candy_price
    result = candy_count
    return result

print(solution())