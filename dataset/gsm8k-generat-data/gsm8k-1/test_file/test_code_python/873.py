def solution():
    """To make a profit of $2000, Isaias has to sell the chickens he planned to take to the market from his farm at $50 per chicken. If Isaias has 300 chickens on his farm and plans to sell 3/5 of them, for how much money did Isaias buy the chicken he took to the market for sale?"""
    planned_profit = 2000
    price_per_chicken = 50
    total_chickens = 300
    chickens_to_sell = total_chickens * (3/5)
    total_sales = planned_profit + (chickens_to_sell * price_per_chicken)
    cost_per_chicken = (total_sales/planned_profit) - price_per_chicken
    total_cost = cost_per_chicken * total_chickens
    result = total_cost
    return result

print(solution())