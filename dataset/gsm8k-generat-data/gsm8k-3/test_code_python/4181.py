def solution():
    """Hannah wants to save $80 for five weeks. In the first week, she saved $4 and she plans to save twice as much as her savings as the previous week. How much will she save in the fifth week to reach her goal?"""
    # Define the total amount to be saved and the first week's savings
    total_savings = 80
    week1_savings = 4

    # Calculate the remaining amount to be saved
    remaining_savings = total_savings - week1_savings

    # Define a variable for the current week's savings
    current_savings = week1_savings

    # Loop through the remaining weeks and calculate the savings for each week
    for i in range(2, 6):
        current_savings *= 2  # double the savings from the previous week
        remaining_savings -= current_savings  # subtract the current week's savings from the remaining amount

    # Display the amount to be saved in the final week
    result = remaining_savings
    return result

print(solution())