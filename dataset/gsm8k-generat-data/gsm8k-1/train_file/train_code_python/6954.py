def solution():
    """Carlo has a music recital next week. He practiced twice as long on Monday as on Tuesday. On Tuesday, he practiced 10 minutes less than on Wednesday. On Wednesday, he practiced 5 minutes more than on Thursday. On Thursday, he practiced for 50 minutes. If he needs to practice for a total of 5 hours that week, how long should Carlo practice on Friday?"""
    thursday_minutes = 50
    wednesday_minutes = thursday_minutes + 5
    tuesday_minutes = wednesday_minutes - 10
    monday_minutes = tuesday_minutes * 2
    total_minutes_practiced = monday_minutes + tuesday_minutes + wednesday_minutes + thursday_minutes
    minutes_left_for_friday = (5 * 60) - total_minutes_practiced
    result = minutes_left_for_friday
    return result

print(solution())