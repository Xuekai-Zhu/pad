def solution():
    """In a car dealership, Fiona worked for 40 hours a week, John for 30 hours, and Jeremy for 25 hours. If the employees are paid $20 per hour, how much money does their boss spend paying all of them every month?"""
    fiona_hours = 40
    john_hours = 30
    jeremy_hours = 25
    hourly_rate = 20
    total_hours = fiona_hours + john_hours + jeremy_hours
    total_pay = total_hours * hourly_rate * 4  # 4 weeks in a month
    result = total_pay
    return result

print(solution())