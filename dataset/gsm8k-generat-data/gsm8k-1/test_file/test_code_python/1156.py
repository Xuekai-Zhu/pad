def solution():
    """Last week the IRS received 5168 tax reports. On Monday and Tuesday they received a total of 1907 reports. On Thursday and Friday they received a total of 2136 reports. How many reports did they receive on Wednesday?"""
    total_reports = 5168
    monday_tuesday_reports = 1907
    thursday_friday_reports = 2136
    wednesday_reports = total_reports - monday_tuesday_reports - thursday_friday_reports
    result = wednesday_reports
    return result

print(solution())