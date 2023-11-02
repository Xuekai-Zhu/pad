def solution():
    """In a car dealership, Fiona worked for 40 hours a week, John for 30 hours, and Jeremy for 25 hours. If the employees are paid $20 per hour, how much money does their boss spend paying all of them every month?"""
    fiona_hours_per_week = 40
    john_hours_per_week = 30
    jeremy_hours_per_week = 25
    hourly_rate = 20
    total_hours_per_week = fiona_hours_per_week + john_hours_per_week + jeremy_hours_per_week
    total_monthly_pay = total_hours_per_week * hourly_rate * 4
    result = total_monthly_pay
    return result

print(solution())