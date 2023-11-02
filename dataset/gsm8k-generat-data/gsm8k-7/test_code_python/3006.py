def solution():
    total_flavors = 100
    flavors_tried_last_year = (1/4) * total_flavors * 2
    flavors_left_to_try = total_flavors - flavors_tried_last_year
    result = flavors_left_to_try
    return result

print(solution())