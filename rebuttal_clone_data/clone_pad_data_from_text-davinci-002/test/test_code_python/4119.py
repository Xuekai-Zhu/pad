def solution():
    fries_per_potato = 25
    total_potatoes = 15
    total_fries_needed = 200
    total_fries_possible = total_potatoes * fries_per_potato
    leftover_fries = total_fries_possible - total_fries_needed
    leftover_potatoes = leftover_fries / fries_per_potato
    result = leftover_potatoes
    return result

print(solution())