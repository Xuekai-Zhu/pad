def solution():
     """James buys 5 packs of beef that are 4 pounds each. The price of beef is $5.50 per pound. How much did he pay?"""
     number_of_packs = 5
     pounds_per_pack = 4
     price_per_pound = 5.50
     total_pounds = number_of_packs * pounds_per_pack
     total_cost = total_pounds * price_per_pound
     result = total_cost
     return result

print(solution())