def solution():
    """At a flea market, Hillary sells handmade crafts for 12 dollars per craft. Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. Later on, Hillary deposits 18 dollars from today's profits into her bank account. How many dollars is Hillary left with after making the deposit?"""
    craft_price = 12
    sold_crafts = 3
    extra_money = 7
    total_profit = (sold_crafts * craft_price) + extra_money
    deposit_amount = 18
    left_amount = total_profit - deposit_amount
    result = left_amount
    return result

print(solution())