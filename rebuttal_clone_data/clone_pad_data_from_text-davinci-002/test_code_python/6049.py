def solution():
     price_cherries = 5
     price_olives = 7
     number_of_bags = 50
     discount = 10
 
     total_cost = (price_cherries * number_of_bags) + (price_olives * number_of_bags)
     total_discount = total_cost * (discount / 100)
     final_cost = total_cost - total_discount
 
     result = final_cost
     return result

print(solution())