def solution():
    
    total_cars = 20
    automatic_cars = 12
    manual_cars = 4
    semi_automatic_cars = total_cars - automatic_cars - manual_cars
    percentage_semi_automatic = (semi_automatic_cars / total_cars) * 100
    result = percentage_semi_automatic
    return result

print(solution())