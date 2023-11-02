def solution():
    
    total_cars = 300
    valid_tickets = 0.75 * total_cars
    permanent_passes = valid_tickets / 5
    unpaid_cars = total_cars - (valid_tickets + permanent_passes)
    result = unpaid_cars
    return result

print(solution())