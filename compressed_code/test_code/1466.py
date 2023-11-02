def solution():
    
    total_cars = 500
    salespeople = 10
    cars_sold_per_month = 10
    total_cars_sold_per_month = salespeople * cars_sold_per_month
    months_to_sell_all_cars = total_cars / total_cars_sold_per_month
    result = months_to_sell_all_cars
    return result

print(solution())