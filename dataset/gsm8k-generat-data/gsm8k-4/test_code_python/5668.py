def solution():
    """Stacy bought two packs of printer paper for the office. Each pack has 240 sheets of paper. Her office prints 80 one-page documents per day. How many days will the printer paper last her office?"""
    # Define the number of sheets per pack and the number of sheets printed per day
    SHEETS_PER_PACK = 240
    SHEETS_PER_DAY = 80

    # Calculate the total number of sheets of paper
    total_sheets = SHEETS_PER_PACK * 2

    # Calculate the number of days the printer paper will last
    days = total_sheets // (SHEETS_PER_DAY)

    # Return the result
    return days

print(solution())