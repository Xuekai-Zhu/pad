def solution():
    # Calculate the total number of hours John streams per week
    streaming_hours = (7 - 3) * 4  # John takes 3 days off, so he streams 4 hours/day for the remaining 4 days

    # Calculate the total amount of money John makes per week
    weekly_pay = streaming_hours * 10  # John makes $10 per hour of streaming

    result = weekly_pay
    return result

print(solution())