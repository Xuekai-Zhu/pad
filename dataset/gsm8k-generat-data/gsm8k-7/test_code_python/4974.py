def solution():
    days_streaming = 7 - 3  # John takes 3 days off, so he streams 7-3=4 days per week
    hours_streaming = 4
    hourly_rate = 10

    # Calculate the total number of hours John streams in a week
    total_hours = days_streaming * hours_streaming

    # Calculate John's total earnings for the week
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())