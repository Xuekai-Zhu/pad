def solution():
     dorothy_pens = 2
     julia_pens = dorothy_pens * 2
     robert_pens = julia_pens / 3
     total_pens = dorothy_pens + julia_pens + robert_pens
     pen_price = 1.50
     total_spent = total_pens * pen_price
     result = total_spent
     return result

print(solution())