def solution():
    total_sheets = 2450
    num_binders = 5
    justine_binder = 1
    colored_percent = 0.5

    # Calculate the number of sheets of paper per binder
    sheets_per_binder = total_sheets / num_binders

    # Calculate the number of sheets of paper Justine used
    sheets_used = sheets_per_binder * colored_percent

    result = sheets_used
    return result

print(solution())