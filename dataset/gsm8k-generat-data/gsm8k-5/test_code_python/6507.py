def solution():
    total_sheets = 2450  # There are 2450 sheets of paper

    # Divide the total number of sheets evenly into 5 binders
    sheets_per_binder = total_sheets / 5
    # Justine took one binder, so she has access to sheets_per_binder number of sheets

    # Justine colored on half of the sheets she had access to
    colored_sheets = sheets_per_binder / 2
    result = colored_sheets
    return result

print(solution())