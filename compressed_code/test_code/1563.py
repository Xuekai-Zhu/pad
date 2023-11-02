def solution():
    
    heated_tanks = 3
    heated_tank_capacity = 15
    remaining_fish = 75 - (heated_tanks * heated_tank_capacity)
    additional_tanks_capacity = 10
    additional_tanks_needed = remaining_fish // additional_tanks_capacity
    if remaining_fish % additional_tanks_capacity != 0:
        additional_tanks_needed += 1

    result = additional_tanks_needed
    return result

print(solution())