def solution():
    """There were 2450 sheets of paper that were evenly split into 5 binders. Justine took a binder and colored on one-half of the sheets of paper. How many sheets of paper did Justine use?"""
    total_sheets = 2450
    num_binders = 5
    sheets_per_binder = total_sheets / num_binders
    colored_sheets = sheets_per_binder / 2
    result = colored_sheets
    return result

print(solution())