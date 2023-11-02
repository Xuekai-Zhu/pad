def solution():
    
    carlos_rental_rate = 30
    benji_rental_rate = 18
    boat_hours = 3
    benji_hours = 5
    carlos_rental = carlos_rental_rate * boat_hours
    benji_rental = benji_rental_rate * benji_hours
    total_rental = carlos_rental + benji_rental
    result = total_rental
    return result

print(solution())