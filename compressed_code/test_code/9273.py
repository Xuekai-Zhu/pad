def solution():
    
    num_phones = 3
    phone_cost = 600
    total_cost = num_phones * phone_cost
    discount_threshold = 2
    discount_percent = 5
    if num_phones >= discount_threshold:
        total_cost *= (100 - discount_percent) / 100
    individual_cost = phone_cost
    individual_total_cost = individual_cost * num_phones
    saved_amount = individual_total_cost - total_cost
    result = saved_amount
    return result

print(solution())