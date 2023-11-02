def solution():
     total_cost = 54
     discount_percent = 20
     coupon_percent = 10
     item_ cost = 20
     new_item_cost = item_cost - (item_cost * (discount_percent / 100))
     total_cost_after_discount = total_cost - (new_item_cost * (coupon_percent / 100))
 
    return total_cost_after_discount

print(solution())