def solution():
    initial_customers = 175
    increase_percentage = 100
    increased_customers = initial_customers * (increase_percentage / 100)
    total_customers = initial_customers + increased_customers
    customers_in_8_hours = total_customers * 8
    result = customers_in_8_hours
    return result

print(solution())