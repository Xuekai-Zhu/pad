def solution():
    """After uploading her video to Youtube, Kallie received 4000 views on the first day. When she checked her channel 4 days later, she realized that the number of views had increased by a number ten times more than the views on the first day. If 50000 more people viewed the video after another two days, determine the number of views the video had gained on Youtube?"""
    # Define the initial number of views
    initial_views = 4000

    # Calculate the number of views gained after 4 days
    views_after_4_days = initial_views + (initial_views * 10 * 4)

    # Calculate the total number of views after 6 days
    total_views = views_after_4_days + 50000

    # Calculate the number of views gained
    views_gained = total_views - initial_views

    # return the result
    result = views_gained
    return result

print(solution())