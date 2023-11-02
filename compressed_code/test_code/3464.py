def solution():
    
    daily_paper_use = 200
    weekly_paper_use = 9000
    school_days = 5
    total_paper_use = weekly_paper_use / school_days
    classes = total_paper_use / daily_paper_use
    result = classes
    return result

print(solution())