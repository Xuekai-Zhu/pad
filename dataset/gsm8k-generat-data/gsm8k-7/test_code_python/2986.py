def solution():
    cost_per_phone = 800
    num_phones = 2
    discount = 0.05 # 5% discount

    # Calculate the total cost of two phones before discount
    total_cost_before_discount = cost_per_phone * num_phones

    # Calculate the amount of discount
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())