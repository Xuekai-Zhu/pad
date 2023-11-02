def solution():
    
    total_sheets = 2450
    binders = 5
    sheets_per_binder = total_sheets / binders
    colored_sheets = sheets_per_binder / 2
    result = colored_sheets
    return result

print(solution())