def solution():
    """Kiki likes to spend her money on hats and scarves. When she buys twice as many hats as scarves, she spends 60% of her money on hats and the rest on scarves. If she currently has $90, how many scarves will she buy if they are sold at $2 each?"""
    total_money = 90
    percent_spent_on_hats = 60
    percent_spent_on_scarves = 100 - percent_spent_on_hats
    spent_on_hats = total_money * (percent_spent_on_hats / 100)
    spent_on_scarves = total_money - spent_on_hats
    price_per_scarf = 2
    num_hats = 2
    num_scarves = spent_on_scarves / price_per_scarf
    result = num_scarves
    return result

print(solution())