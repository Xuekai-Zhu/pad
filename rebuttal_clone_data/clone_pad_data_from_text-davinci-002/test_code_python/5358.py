def solution():
    cost_per_item = 0.4
    quantity_purchased = 400
   discount_rate = 2
    qualifying_purchase = 10
    total_cost = cost_per_item * quantity_purchased
    discount_amount = total_cost / qualifying_purchase * discount_rate
    final_cost = total_cost - discount_amount
    result = final_cost
    return result

print(solution())