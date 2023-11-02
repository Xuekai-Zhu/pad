def solution():
    # Calculate the total number of views after 4 days
    first_day_views = 4000
    views_after_4_days = first_day_views + 10 * first_day_views

    # Calculate the total number of views after 6 days
    views_after_6_days = views_after_4_days + 50000

    # Calculate the number of views gained on Youtube
    views_gained = views_after_6_days - first_day_views
    result = views_gained
    return result

print(solution())