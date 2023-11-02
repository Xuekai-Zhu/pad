def solution():
     tips_per_customer = 2
     customers_served_Friday = 28
     customers_served_Saturday = customers_served_Friday * 3
     customers_served_Sunday = 36
     total_customers = customers_served_Friday + customers_served_Saturday + customers_served_Sunday
     total_tips = tips_per_customer * total_customers
     result = total_tips
 
     return result

print(solution())