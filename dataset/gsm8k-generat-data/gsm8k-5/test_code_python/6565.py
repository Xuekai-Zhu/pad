def solution():
    session_fee = 20  # Gnuff charges a flat rate of $20 per tutoring session
    total_fee = 146  # The total amount paid for Gnuff for tutoring for one session is $146
    per_minute_fee = total_fee - session_fee  # Deduct the session fee to get the amount paid for minutes
    minutes_tutored = per_minute_fee / 7  # Divide the per minute fee by the charge per minute
    
    result = minutes_tutored
    return result

print(solution())