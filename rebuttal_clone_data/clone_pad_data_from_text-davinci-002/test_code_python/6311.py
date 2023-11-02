def solution():
     purchase_price = ((12 * 3) + (5 * 1) + (15 * 2) + (14 * 1))
     if purchase_price < 50:
         shipping_cost = 5
     else:
         shipping_cost = purchase_price * .2
     total_bill = purchase_price + shipping_cost
     result = total_bill
     return result

print(solution())