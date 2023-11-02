def solution():
    """To support the school outreach program, Einstein wants to raise $500 by selling snacks. One box of pizza sells for $12, a pack of potato fries sells for $0.30, and a can of soda at $2. Einstein sold 15 boxes of pizzas, 40 packs of potato fries, and 25 cans of soda. How much more money does Einstein need to raise to reach his goal?"""
    pizza_price = 12
    fries_price = 0.30
    soda_price = 2
    total_sales = (pizza_price * 15) + (fries_price * 40) + (soda_price * 25)
    goal_amount = 500
    money_needed = goal_amount - total_sales
    result = money_needed
    return result

print(solution())