def solution():
    
    total_cakes = 60
    cakes_made = total_cakes / 2
    cakes_left = total_cakes - cakes_made
    first_day_cakes = cakes_left / 2
    cakes_left = cakes_left - first_day_cakes
    second_day_cakes = cakes_left / 3
    total_cakes_needed = cakes_made + first_day_cakes + second_day_cakes
    more_cakes_needed = total_cakes - total_cakes_needed
    result = more_cakes_needed
    return result

print(solution())