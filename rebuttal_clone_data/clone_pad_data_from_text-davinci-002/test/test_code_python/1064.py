def solution():
    total_cars = 500
    sales_professionals = 10
    cars_sold_per_month = 10
    total_cars_sold = sales_professionals * cars_sold_per_month
    months_needed = total_cars / total_cars_sold
    result = months_needed
    
    return result

print(solution())