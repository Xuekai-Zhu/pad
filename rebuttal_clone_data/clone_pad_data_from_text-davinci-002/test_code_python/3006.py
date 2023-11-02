def solution():
    total_flavors = 100
    flavors_tried_2_years_ago = total_flavors / 4
    flavors_tried_last_year = flavors_tried_2_years_ago * 2
    flavors_tried_this_year = flavors_tried_last_year + (total_flavors - flavors_tried_last_year)
    result = flavors_tried_this_year - total_flavors
    return result

print(solution())