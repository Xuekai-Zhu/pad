def solution():
    
    car_patrons = 12
    bus_patrons = 27
    total_patrons = car_patrons + bus_patrons
    carts_needed = total_patrons // 3
    if total_patrons % 3 != 0:
        carts_needed += 1

    result = carts_needed
    return result

print(solution())