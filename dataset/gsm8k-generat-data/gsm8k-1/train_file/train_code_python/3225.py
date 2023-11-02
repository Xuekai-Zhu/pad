def solution():
    """Wade has a hot dog food truck. He makes $2.00 in tips per customer. On Friday he served 28 customers. He served three times that amount of customers on Saturday. On Sunday, he served 36 customers. How many dollars did he make in tips between the 3 days?"""
    friday_customers = 28
    saturday_customers = 3 * friday_customers
    sunday_customers = 36
    tips_per_customer = 2
    total_tips = (friday_customers + saturday_customers + sunday_customers) * tips_per_customer
    result = total_tips
    return result

print(solution())