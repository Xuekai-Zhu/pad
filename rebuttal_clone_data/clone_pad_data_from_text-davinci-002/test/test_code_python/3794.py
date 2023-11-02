def solution():
    total_cars = 3000
    cars_15000_or_less = total_cars * .15
    cars_20000_or_more = total_cars * .40
    cars_15000_to_20000 = total_cars - (cars_15000_or_less + cars_20000_or_more)
    result = cars_15000_to_20000
    return result

print(solution())