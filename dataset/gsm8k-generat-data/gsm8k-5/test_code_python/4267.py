def solution():
    # Calculate the number of views after 4 days
    views_after_4_days = 4000 * 10  # The number of views increased by 10 times after 4 days

    # Calculate the total number of views after 6 days
    total_views = views_after_4_days + 50000  # 50000 more people viewed the video after another 2 days

    # Calculate the number of views gained on Youtube
    views_gained = total_views - 4000  # The video had 4000 views on the first day

    result = views_gained
    return result

print(solution())