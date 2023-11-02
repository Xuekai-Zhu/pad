def solution():
    """At a flea market, Hillary sells handmade crafts for 12 dollars per craft. Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. Later on, Hillary deposits 18 dollars from today's profits into her bank account. How many dollars is Hillary left with after making the deposit?"""
    price_per_craft = 12
    num_crafts_sold = 3
    extra_money = 7
    total_money = (price_per_craft * num_crafts_sold) + extra_money
    deposit = 18
    remaining_money = total_money - deposit
    result = remaining_money
    
    return result

print(solution())