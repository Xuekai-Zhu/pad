def solution():
    cost_hand_mitts = 14
    cost_apron = 16
    cost_utensils = 10
    cost_knife = cost_utensils * 2
    discount_rate = 25
    total_cost = cost_hand_mitts + cost_apron + cost_utensils + cost_knife
    discount_amount = total_cost * (discount_rate / 100)
    cost_after_discount = total_cost - discount_amount
    result = cost_after_discount
    return result

print(solution())