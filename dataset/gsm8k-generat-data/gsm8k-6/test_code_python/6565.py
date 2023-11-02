def solution():
    # Calculate the number of minutes Gnuff tutored for
    total_paid = 146  # total amount paid for one tutoring session
    flat_rate = 20  # flat rate charged per tutoring session
    per_minute_rate = 7  # rate charged per minute of tutoring
    minutes_tutored = (total_paid - flat_rate) / per_minute_rate
    result = minutes_tutored
    return result

print(solution())