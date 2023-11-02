def solution():
    """Stacy bought two packs of printer paper for the office. Each pack has 240 sheets of paper. Her office prints 80 one-page documents per day. How many days will the printer paper last her office?"""
    sheets_per_pack = 240
    packs_of_paper = 2
    sheets_per_day = 80
    total_sheets = sheets_per_pack * packs_of_paper
    days_of_paper = total_sheets // sheets_per_day
    result = days_of_paper
    return result

print(solution())