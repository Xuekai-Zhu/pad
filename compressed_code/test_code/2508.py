def solution():
    
    friday_customers = 28
    saturday_customers = friday_customers * 3
    sunday_customers = 36
    total_customers = friday_customers + saturday_customers + sunday_customers
    tips_per_customer = 2
    total_tips = total_customers * tips_per_customer
    result = total_tips
    return result

print(solution())