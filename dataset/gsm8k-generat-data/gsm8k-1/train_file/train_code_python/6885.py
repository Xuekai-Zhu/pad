def solution():
    """A baseball cap factory made 320 caps the first week, 400 the second week, and 300 the third week. If the company makes their average number of caps from the first 3 weeks during the fourth week, how many total caps will they make?"""
    first_week_caps = 320
    second_week_caps = 400
    third_week_caps = 300
    total_caps = first_week_caps + second_week_caps + third_week_caps
    average_caps = total_caps / 3
    total_caps += average_caps
    result = total_caps
    return result

print(solution())