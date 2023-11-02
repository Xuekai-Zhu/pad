def solution():
    """Lanie has been sick and was only able to work 4/5 of her usual 40-hour week. If her hourly rate is $15, how much was her salary for that week?"""
    usual_hours = 40
    worked_hours = usual_hours * (4/5)
    hourly_rate = 15
    salary = worked_hours * hourly_rate
    result = salary
    return result

print(solution())