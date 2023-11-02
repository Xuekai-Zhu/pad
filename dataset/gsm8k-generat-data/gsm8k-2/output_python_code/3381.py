def solution():
    """Andrew works in a company that provides a generous vacation allotment: for every 10 days worked, 
    you get 1 vacation day. If last year Andrew worked 300 days and took 5 days off in March and twice 
    as many in September, how many more vacation days can Andrew still take?"""
    worked_days = 300
    vacation_days_earned = worked_days // 10
    march_vacation_days = 5
    september_vacation_days = 2 * 5
    total_vacation_days_taken = march_vacation_days + september_vacation_days
    remaining_vacation_days = vacation_days_earned - total_vacation_days_taken
    result = remaining_vacation_days
    return result

print(solution())