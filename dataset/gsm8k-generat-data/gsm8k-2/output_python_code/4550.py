def solution():
    """Maria's birthday is in 22 days. Her friend Lilly wants to buy her flowers so she saves $2 each day until Maria's birthday. If a flower costs $4, how many flowers can she buy?"""
    days_until_birthday = 22
    money_saved_per_day = 2
    flower_price = 4
    total_money_saved = days_until_birthday * money_saved_per_day
    total_flowers = total_money_saved // flower_price
    result = total_flowers
    return result

print(solution())