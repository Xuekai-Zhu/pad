def solution():
    """Each class uses 200 sheets of paper per day. The school uses a total of 9000 sheets of paper every week. If there are 5 days of school days, how many classes are there in the school?"""
    daily_paper_use = 200
    weekly_paper_use = 9000
    school_days = 5
    total_paper_use = weekly_paper_use / school_days
    classes = total_paper_use / daily_paper_use
    result = classes
    return result

print(solution())