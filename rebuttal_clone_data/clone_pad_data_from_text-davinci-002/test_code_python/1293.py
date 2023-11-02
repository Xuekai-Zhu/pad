def solution():
     jimmy_item_quantity = 3
     irene_item_quantity = 5
     jimmy_item_cost = 15
     irene_item_cost = 17
     percent_discount = 10
     jimmy_item_total = jimmy_item_cost * jimmy_item_quantity
     irene_item_total = irene_item_cost * irene_item_quantity
     jimmy_discount = jimmy_item_total * (percent_discount / 100)
     irene_discount = irene_item_total * (percent_discount / 100)
     total_before_tax = (jimmy_item_total - jimmy_discount) + (irene_item_total - irene_discount)
     result = total_before_tax
     return result

print(solution())