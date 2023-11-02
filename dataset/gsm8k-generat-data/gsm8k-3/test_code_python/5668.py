def solution():
    """Stacy bought two packs of printer paper for the office. Each pack has 240 sheets of paper. Her office prints 80 one-page documents per day. How many days will the printer paper last her office?"""
    # Define the number of sheets of paper per pack
    SHEETS_PER_PACK = 240

    # Calculate the total number of sheets of paper
    total_sheets = SHEETS_PER_PACK * 2

    # Calculate the number of days the paper will last
    sheets_per_day = 80
    days_of_paper = total_sheets / sheets_per_day

    # Display the number of days the paper will last
    result = days_of_paper
    return result

print(solution())