def solution():
    
    total_cars = 300
    valid_tickets = int(total_cars * 0.75)
    permanent_passes = int(valid_tickets * 0.2)
    cars_without_payment = total_cars - valid_tickets - permanent_passes
    result = cars_without_payment
    return result

print(solution())