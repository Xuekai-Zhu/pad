def solution():
     bulk_price = 5
     minimum_spend = 40
     tax = 1
     purchase_price = 240
     minimum_purchase = minimum_spend + (minimum_spend * tax)
     pounds_purchased = purchase_price / bulk_price
     result = pounds_purchased - minimum_purchase
     return result

print(solution())