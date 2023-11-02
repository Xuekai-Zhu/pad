def solution():
    # Calculate the number of views after 4 days
    views_after_4_days = 4000 * 10

    # Calculate the total number of views after 6 days
    total_views = views_after_4_days + 4000 + 50000

    # Calculate the number of views gained on Youtube
    views_gained = total_views - 4000
    result = views_gained
    return result

print(solution())