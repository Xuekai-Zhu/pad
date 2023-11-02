def solution():
    """Stacy bought two packs of printer paper for the office. Each pack has 240 sheets of paper. Her office prints 80 one-page documents per day. How many days will the printer paper last her office?"""
    num_of_packs = 2
    sheets_per_pack = 240
    total_sheets = num_of_packs * sheets_per_pack
    sheets_per_day = 80
    days_of_use = total_sheets // sheets_per_day
    result = days_of_use
    return result

print(solution())