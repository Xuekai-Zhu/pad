def solution():
    
    cars_per_day = 80
    price_per_car = 5
    days = 5
    total_cars_washed = cars_per_day * days
    total_money_made = total_cars_washed * price_per_car
    result = total_money_made
    return result

print(solution())