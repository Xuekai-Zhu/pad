def solution():
    # Calculate the total number of papers that Kyle delivers each week
    daily_papers = 100 * 6  # he delivers the daily paper for 100 houses from Monday-Saturday
    sunday_papers = 100 - 10 + 30  # 10 houses do not get the Sunday paper, but he delivers 30 papers to other houses that get the newspaper only on Sunday
    total_papers = daily_papers + sunday_papers  # total number of papers Kyle delivers each week
    result = total_papers
    return result

print(solution())