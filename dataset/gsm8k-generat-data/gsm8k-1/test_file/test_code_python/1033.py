def solution():
    """The price of Parmesan cheese is $11 per pound. Mozzarella cheese is $6 per pound. Amor buys 2 pounds of Parmesan and 3 pounds of mozzarella cheese. If she starts with $50 cash, how much money, in dollars, will she have left to buy meat?"""
    parmesan_price = 11
    mozzarella_price = 6
    parmesan_weight = 2
    mozzarella_weight = 3
    total_cost = (parmesan_price * parmesan_weight) + (mozzarella_price * mozzarella_weight)
    starting_cash = 50
    money_left = starting_cash - total_cost
    result = money_left
    return result

print(solution())