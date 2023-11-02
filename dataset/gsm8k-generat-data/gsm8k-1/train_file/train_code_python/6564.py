def solution():
    """Gnuff charges a flat rate of $20 per tutoring session plus $7 per minute. The total amount paid for Gnuff for tutoring for one session is $146. How many minutes did Gnuff tutor for?"""
    flat_rate = 20
    total_paid = 146
    per_minute = 7
    minutes_tutored = (total_paid - flat_rate) / per_minute
    result = minutes_tutored
    return result

print(solution())