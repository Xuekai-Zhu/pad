def solution():
    
    total_earned = 45
    cars_sold = 3
    car_price = 5
    cars_total = cars_sold * car_price
    legos_price = total_earned - cars_total
    result = legos_price
    return result

print(solution())