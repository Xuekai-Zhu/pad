def solution():
    first_day_views = 4000
    views_increase_factor = 10
    second_day_views = first_day_views * views_increase_factor
    third_day_views = second_day_views * views_increase_factor
    fourth_day_views = third_day_views * views_increase_factor
    fifth_day_views = fourth_day_views + 50000

    total_views = first_day_views + second_day_views + third_day_views + fourth_day_views + fifth_day_views
    views_gained = total_views - first_day_views
    result = views_gained
    return result

print(solution())