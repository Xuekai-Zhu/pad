def solution():
    cakes_needed = 60
    cakes_made = cakes_needed / 2
    cakes_left = cakes_needed - cakes_made
    cakes_left_after_1st_day = cakes_left / 2
    cakes_left_after_2nd_day = cakes_left_after_1st_day / 3
    cakes_to_be_made = cakes_left_after_2nd_day
    result = cakes_to_be_made
    return result

print(solution())