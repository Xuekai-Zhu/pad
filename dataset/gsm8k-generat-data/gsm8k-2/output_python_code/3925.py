def solution():
    """Fred had 212 sheets of paper. He received another 307 sheets of paper from Jane and gave Charles 156 sheets of paper. How many sheets of paper does Fred have left?"""
    fred_sheets = 212
    jane_sheets = 307
    charles_sheets = 156
    fred_sheets += jane_sheets
    fred_sheets -= charles_sheets
    result = fred_sheets
    return result

print(solution())