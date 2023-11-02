def solution():
    """Each class uses 200 sheets of paper per day. The school uses a total of 9000 sheets of paper every week. If there are 5 days of school days, how many classes are there in the school?"""
    sheets_per_day = 200
    sheets_per_week = sheets_per_day * 5
    total_classes = 9000 / sheets_per_week
    result = total_classes
    return result

print(solution())