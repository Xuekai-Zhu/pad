def solution():
    """While at the dollar store, Sloane counts 100 customers entering the store. The next day, she counts 50 more customers than the first day. If the total number of customers by the third day was 500, how many customers did she count on the third day?"""
    day1_customers = 100
    day2_customers = day1_customers + 50
    total_customers = 500
    day3_customers = total_customers - (day1_customers + day2_customers)
    result = day3_customers
    return result

print(solution())