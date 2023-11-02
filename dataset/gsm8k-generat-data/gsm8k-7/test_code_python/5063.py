def solution():
    notes_per_day = 2
    days_per_week = 5
    classes_per_day = 5
    sheets_per_pack = 100
    weeks = 6

    # Calculate the total number of sheets of paper Chip will use in one day
    daily_sheets = notes_per_day * classes_per_day

    # Calculate the total number of sheets of paper Chip will use in one week
    weekly_sheets = daily_sheets * days_per_week

    # Calculate the total number of sheets of paper Chip will use in six weeks
    total_sheets = weekly_sheets * weeks

    # Calculate the number of packs of paper Chip will need
    packs_needed = total_sheets // sheets_per_pack  # Use integer division to round down

    result = packs_needed
    return result

print(solution())