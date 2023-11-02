def solution():
    """After uploading her video to Youtube, Kallie received 4000 views on the first day. When she checked her channel 4 days later, 
    she realized that the number of views had increased by a number ten times more than the views on the first day. 
    If 50000 more people viewed the video after another two days, determine the number of views the video had gained on Youtube?"""
    
    # calculate total number of views after 4 days
    day1_views = 4000
    day5_views = day1_views + 10 * day1_views
    day7_views = day5_views + 50000
    
    gained_views = day7_views - day1_views   # calculate number of views the video gained on Youtube
    
    result = gained_views
    return result

print(solution())