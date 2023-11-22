def solution():
    
    # Define the number of sheets of paper on a pad of paper
    SHEETS_PER_PAD = 30

    # Define the number of pads of paper Miguel uses per week
    pads_per_week = 2

    # Calculate the total number of sheets of paper Miguel uses per week
    total_sheets_per_week = pads_per_week * SHEETS_PER_PAD

    # Calculate the total number of sheets of paper Miguel uses per month
    total_sheets_per_month = total_sheets_per_week * 4

    # Display the total number of sheets of paper Miguel uses per month
    result = total_sheets_per_month
    return result

print(solution())