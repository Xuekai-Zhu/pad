def solution():
    """Maia is a freelance blogger working for different clients for whom she writes different articles every day. She gets 6 client requests every day and works on four of them each day. How many client requests will she have remaining to work on after 5 days?"""
    daily_requests = 6
    daily_completed = 4
    remaining = daily_requests - daily_completed
    remaining_after_5_days = remaining * 5
    result = remaining_after_5_days
    return result

print(solution())