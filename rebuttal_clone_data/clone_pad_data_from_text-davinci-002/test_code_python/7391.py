def solution():
    washer_cost = 4
    dryer_cost = 0.25
    loads_of_laundry = 2
    minutes_in_dryer = 40
    total_cost = washer_cost + (dryer_cost * (loads_of_laundry * (minutes_in_dryer / 10)))
    result = total_cost
    return result

print(solution())