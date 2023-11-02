def solution():
    hours_worked = 8
    customers_per_hour = 7
    hours_worked_by_julia = 6
    customers_served_by_ann = hours_worked * customers_per_hour
    customers_served_by_becky = customers_served_by_ann
    customers_served_by_julia = hours_worked_by_julia * customers_per_hour
    total_customers = customers_served_by_ann + customers_served_by_becky + customers_served_by_julia
    result = total_customers
    
    return result

print(solution())