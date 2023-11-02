def solution():
    """Andrew works in a company that provides a generous vacation allotment: for every 10 days worked, you get 1 vacation day. If last year Andrew worked 300 days and took 5 days off in March and twice as many in September, how many more vacation days can Andrew still take?"""
    days_worked = 300
    march_days_off = 5
    september_days_off = 2 * march_days_off
    total_days_off = march_days_off + september_days_off
    vacation_days_earned = days_worked // 10
    vacation_days_taken = total_days_off
    vacation_days_remaining = vacation_days_earned - vacation_days_taken
    result = vacation_days_remaining
    return result

print(solution())