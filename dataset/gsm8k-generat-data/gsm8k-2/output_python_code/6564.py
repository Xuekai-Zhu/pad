def solution():
    """Gnuff charges a flat rate of $20 per tutoring session plus $7 per minute. The total amount paid for Gnuff for tutoring for one session is $146. How many minutes did Gnuff tutor for?"""
    total_paid = 146
    flat_rate = 20
    per_minute_rate = 7
    minutes_tutored = (total_paid - flat_rate) / per_minute_rate
    result = minutes_tutored
    return result

print(solution())