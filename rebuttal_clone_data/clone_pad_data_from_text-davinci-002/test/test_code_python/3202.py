def solution():
    sheets_of_paper = 240
    documents_per_day = 80
    sheets_needed_per_day = documents_per_day
    total_sheets = sheets_of_paper * 2
    total_days = total_sheets / sheets_needed_per_day
    result = total_days
    return result

print(solution())