def solution():
    """After uploading her video to Youtube, Kallie received 4000 views on the first day. When she checked her channel 4 days later, she realized that the number of views had increased by a number ten times more than the views on the first day. If 50000 more people viewed the video after another two days, determine the number of views the video had gained on Youtube?"""
    # Define the number of views on the first day
    day1_views = 4000

    # Calculate the number of views after 4 days
    day5_views = day1_views + day1_views * 10 * 4

    # Calculate the total number of views after 6 days
    day6_views = day5_views + 50000

    # Calculate the number of views gained on Youtube
    total_views_gained = day6_views - day1_views

    # Display the number of views gained
    result = total_views_gained
    return result

print(solution())