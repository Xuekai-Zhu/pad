def solution():
     total_members = 30
     lemon_juice_order = total_members * (2/5)
     mango_juice_order = total_members * (1/3)
     orange_juice_order = total_members - (lemon_juice_order + mango_juice_order)
     result = orange_juice_order
     return result

print(solution())