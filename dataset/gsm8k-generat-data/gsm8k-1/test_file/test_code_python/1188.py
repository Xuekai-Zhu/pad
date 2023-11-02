def solution():
    """Jen works for 7.5 hours a day 6 days a week. Her hourly rate is $1.5. Jen also receives an additional $10 if she has complete attendance. Suppose Jen did not incur any absences for April, and there are exactly 4 weeks in April, how much will she receive?"""
    hours_per_day = 7.5
    days_per_week = 6
    hourly_rate = 1.5
    weeks_in_month = 4
    full_attendance_bonus = 10
    
    total_hours = hours_per_day * days_per_week * weeks_in_month
    hourly_pay = total_hours * hourly_rate
    total_pay = hourly_pay + full_attendance_bonus
    
    result = total_pay
    
    return result

print(solution())