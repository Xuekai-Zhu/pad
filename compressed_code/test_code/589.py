def solution():
    
    total_customers = 25
    coffee_customers = int(total_customers * (3/5))
    non_coffee_customers = total_customers - coffee_customers
    result = non_coffee_customers
    return result

print(solution())