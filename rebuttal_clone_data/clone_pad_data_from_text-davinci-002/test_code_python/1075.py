def solution():
     hoodie_cost = 80
     flashlight_cost = hoodie_cost * 0.2
     boots_cost = 110
     boots_discount = boots_cost * 0.1
     total_cost = hoodie_cost + flashlight_cost + boots_cost - boots_discount
     result = total_cost
     
     return result

print(solution())