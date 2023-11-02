def solution():
    """Fred had 212 sheets of paper. He received another 307 sheets of paper from Jane and gave Charles 156 sheets of paper. How many sheets of paper does Fred have left?"""
    initial_sheets = 212
    additional_sheets = 307
    sheets_given = 156
    final_sheets = initial_sheets + additional_sheets - sheets_given
    result = final_sheets
    return result

print(solution())