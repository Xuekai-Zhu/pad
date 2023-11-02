def solution():
     """At a flea market, Hillary sells handmade crafts for 12 dollars per craft. Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. Later on, Hillary deposits 18 dollars from today's profits into her bank account. How many dollars is Hillary left with after making the deposit?"""
     crafts_sold = 3
     craft_price = 12
     extra_money = 7
     total_money = crafts_sold * craft_price + extra_money
     deposit = 18
     money_left = total_money - deposit
     result = money_left
     return result

print(solution())