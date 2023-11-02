def solution():
    """Miguel uses 2 pads of paper a week for his drawing. If there are 30 sheets of paper on a pad of paper, how many sheets of paper does he use every month?"""
    pads_per_week = 2
    sheets_per_pad = 30
    weeks_per_month = 4
    total_sheets = pads_per_week * sheets_per_pad * weeks_per_month
    result = total_sheets
    return result

print(solution())