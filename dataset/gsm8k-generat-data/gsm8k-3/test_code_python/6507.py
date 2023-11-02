def solution():
    """There were 2450 sheets of paper that were evenly split into 5 binders. Justine took a binder and colored on one-half of the sheets of paper. How many sheets of paper did Justine use?"""
    # Calculate the total number of sheets in one binder
    sheets_per_binder = 2450 / 5

    # Calculate the number of sheets Justine colored on
    colored_sheets = sheets_per_binder / 2

    # Display the number of sheets Justine used
    result = colored_sheets
    return result

print(solution())