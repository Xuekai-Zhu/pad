def solution():
    """Yvette wants to frame a new picture. When she goes to her local frame shop, she finds out that the frame she wanted is 20% more expensive than her budget of $60. If she paid for a smaller frame at 3/4 the new price of the frame she initially intended to buy, how much money did she remain with?"""
    initial_price = 60
    increased_price = initial_price * 1.2
    smaller_price = increased_price * 0.75
    remaining_money = initial_price - smaller_price
    result = remaining_money
    return result

print(solution())