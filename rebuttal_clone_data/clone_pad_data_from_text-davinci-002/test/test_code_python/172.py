def solution():
    seats_per_row = 4
    rows_on_bus = 23
    seats_on_bus = seats_per_row * rows_on_bus
    people_climbing = 16
    people_boarding = 15
    people_leaving = 3
    people_on_bus = people_climbing + people_boarding - people_leaving
    people_boarding = 17
    people_leaving = 10
    people_on_bus = people_on_bus + people_boarding - people_leaving
    seats_left = seats_on_bus - people_on_bus
    result = seats_left
    
    return result

print(solution())