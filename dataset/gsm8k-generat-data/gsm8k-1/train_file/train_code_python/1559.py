def solution():
    """Yvette wants to frame a new picture. When she goes to her local frame shop, she finds out that the frame she wanted is 20% more expensive than her budget of $60. If she paid for a smaller frame at 3/4 the new price of the frame she initially intended to buy, how much money did she remain with?"""
    initial_budget = 60
    percent_increase = 20
    new_price = initial_budget * (1 + (percent_increase / 100))
    smaller_price = new_price * (3 / 4)
    money_left = initial_budget - smaller_price
    result = money_left
    return result

print(solution())