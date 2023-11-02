def solution():
    
    friday_customers = 28
    saturday_customers = 3 * friday_customers
    sunday_customers = 36
    tips_per_customer = 2
    total_tips = (friday_customers + saturday_customers + sunday_customers) * tips_per_customer
    result = total_tips
    return result

print(solution())