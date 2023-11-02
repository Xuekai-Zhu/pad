def solution():
    """After uploading her video to Youtube, Kallie received 4000 views on the first day. When she checked her channel 4 days later, she realized that the number of views had increased by a number ten times more than the views on the first day. If 50000 more people viewed the video after another two days, determine the number of views the video had gained on Youtube?"""
    first_day_views = 4000
    four_day_views = first_day_views + (10 * first_day_views)
    two_day_views = four_day_views + 50000
    total_views = two_day_views - first_day_views
    result = total_views
    return result

print(solution())