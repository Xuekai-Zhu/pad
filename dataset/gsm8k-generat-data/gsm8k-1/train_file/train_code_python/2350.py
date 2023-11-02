def solution():
    """ Lanie has been sick and was only able to work 4/5 of her usual 40-hour week. If her hourly rate is $15, how much was her salary for that week?"""
    usual_hours_per_week = 40
    hour_rate = 15
    sick_hours = usual_hours_per_week * 4/5
    salary = sick_hours * hour_rate
    result = salary
    return result

print(solution())