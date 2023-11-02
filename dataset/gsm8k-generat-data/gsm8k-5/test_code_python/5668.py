def solution():
    packs_of_paper = 2  # Stacy bought 2 packs of printer paper
    sheets_per_pack = 240  # Each pack has 240 sheets of paper
    sheets_per_day = 80  # Her office prints 80 one-page documents per day

    # Calculate the total number of sheets of paper available
    total_sheets = packs_of_paper * sheets_per_pack

    # Calculate the number of days the paper will last
    days = total_sheets // (sheets_per_day * 1)  # using floor division to get an integer value
    result = days
    return result

print(solution())