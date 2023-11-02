def solution():
     breakfast_bagel = 0.95
     breakfast_juice = 0.85
     lunch_sandwich = 4.65
     lunch_milk = 1.15
     breakfast_total = breakfast_bagel + breakfast_juice
     lunch_total = lunch_sandwich + lunch_milk
     difference = lunch_total - breakfast_total
     result = difference
     return result

print(solution())