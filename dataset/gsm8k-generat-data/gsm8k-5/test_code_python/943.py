def solution():
    goal = 96  # Javier wants to raise $96
    cost_per_dozen = 2.4  # Javier buys each dozen donuts for $2.40
    price_per_donut = 1  # Javier sells each donut for $1

    # Calculate the profit Javier makes per donut
    profit_per_donut = price_per_donut - (cost_per_dozen / 12)

    # Calculate the number of donuts Javier needs to sell to reach his goal
    donuts_required = goal / profit_per_donut

    # Calculate the number of dozens of donuts Javier needs to buy and sell
    dozens_required = donuts_required / 12
    result = dozens_required
    return result

print(solution())