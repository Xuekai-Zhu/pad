def solution():
     quarter_weight = 1/5
     ounces_per_pound = 16
     gold_price_per_ounce = 100
     quarter_price = 4
     ounce_price = gold_price_per_pound / ounces_per_pound
     price_difference = ounce_price - quarter_price
     pounds_per_ounce = 1 / ounce_price
     ounce_ounces = quarter_weight * pounds_per_ounce
     result = price_difference / ounce_ounces
     return result

print(solution())