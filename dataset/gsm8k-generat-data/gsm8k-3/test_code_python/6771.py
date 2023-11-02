def solution():
    """Mike decides to do more pull-ups to increase his strength for climbing.  He uses the greasing the groove technique where every time he goes into a certain room he does 2 pull-ups.  He decides to use his office.  He goes in there 5 times a day every day.  How many pull-ups does he do a week?"""
    # Define the number of times Mike goes into his office per day and per week
    DAILY_VISITS = 5
    WEEKLY_VISITS = DAILY_VISITS * 7

    # Define the number of pull-ups Mike does each time he goes into his office
    PULL_UPS_PER_VISIT = 2

    # Calculate the total number of pull-ups Mike does in a week
    total_pull_ups = WEEKLY_VISITS * PULL_UPS_PER_VISIT

    # Display the total number of pull-ups
    result = total_pull_ups
    return result

print(solution())