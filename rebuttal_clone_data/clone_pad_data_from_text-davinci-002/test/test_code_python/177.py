def solution():
    rooms_per_floor = 10
    floors = 4
    hours_per_room = 6
    hourly_wage = 15
    total_hours = rooms_per_floor * floors * hours_per_room
    total_earnings = hourly_wage * total_hours
    result = total_earnings
    return result

print(solution())