def solution():
    cars_per_day = 80
    days = 5
    earning_per_car = 5

    total_cars = cars_per_day * days
    total_earnings = total_cars * earning_per_car
    result = total_earnings
    return result

print(solution())