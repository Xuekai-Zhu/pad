def solution():
    
    extra_cans = 5
    total_cans = 33
    cans_per_customer = 2
    total_customers = (total_cans - extra_cans) / cans_per_customer
    result = total_customers
    return result

print(solution())