def solution():
    
    total_guests = 80
    steak_guests = 3 * total_guests / 4
    chicken_guests = total_guests / 4
    steak_cost = steak_guests * 25
    chicken_cost = chicken_guests * 18
    total_cost = steak_cost + chicken_cost
    result = total_cost
    return result

print(solution())