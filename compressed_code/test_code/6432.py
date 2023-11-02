def solution():
    
    tickets_owned = 5
    ferris_wheel_cost = 5
    roller_coaster_cost = 4
    bumper_cars_cost = 4
    total_cost = ferris_wheel_cost + roller_coaster_cost + bumper_cars_cost
    tickets_needed = total_cost - tickets_owned
    result = tickets_needed
    return result

print(solution())