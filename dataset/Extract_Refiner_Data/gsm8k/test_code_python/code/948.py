def solution():
    
    # Define the number of reports that can be staple in 1 minute
    RECOVERS_PER_MINUTE = 30 / 15

    # Calculate the total number of minutes that Vince was staple
    total_minutes = 8 * 60 + 11 * 60

    # Calculate the total number of reports that Vince staple
    total_reports = RECOVERS_PER_MINUTE * total_minutes

    # Display the total number of reports
    result = total_reports
    return result

print(solution())