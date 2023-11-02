def solution():
    """To support the school outreach program, Einstein wants to raise $500 by selling snacks. One box of pizza sells for $12, a pack of potato fries sells for $0.30, and a can of soda at $2. Einstein sold 15 boxes of pizzas, 40 packs of potato fries, and 25 cans of soda. How much more money does Einstein need to raise to reach his goal?"""
    pizza_price = 12
    fries_price = 0.3
    soda_price = 2
    pizza_sold = 15
    fries_sold = 40
    soda_sold = 25
    total_sales = (pizza_price * pizza_sold) + (fries_price * fries_sold) + (soda_price * soda_sold)
    money_needed = 500
    money_left_to_raise = money_needed - total_sales
    result = money_left_to_raise
    return result

print(solution())