def solution():
    
    monthly_cost = 10
    discount_percentage = 20
    num_months = 12

    total_cost = monthly_cost * num_months
    discount_amount = total_cost * (discount_percentage / 100)
    discounted_total = total_cost - discount_amount

    result = discounted_total
    return result

print(solution())