def solution():
    """Maia is a freelance blogger working for different clients for whom she writes different articles every day. She gets 6 client requests every day and works on four of them each day. How many client requests will she have remaining to work on after 5 days."""
    daily_requests = 6
    requests_worked_on = 4
    remaining_requests_per_day = daily_requests - requests_worked_on
    remaining_requests_after_5_days = remaining_requests_per_day * 5
    result = remaining_requests_after_5_days
    return result

print(solution())