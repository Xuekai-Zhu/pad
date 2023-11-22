def solution():
    
    total_tax_reports = 5168
    monday_tuesday_reports = 1907
    thursday_friday_reports = 2136
    wednesday_reports = total_tax_reports - monday_tuesday_reports - thursday_friday_reports
    result = wednesday_reports
    return result

print(solution())