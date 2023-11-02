def solution():
    morning_hours = 2
    hours_after_school = 2
    hours_on_weekends = 4
    morning_pay = 10
    after_school_pay = 12.50
    weekend_pay = 10
    total_hours = morning_hours + (hours_after_school * 5) + hours_on_weekends
    total_pay = (morning_hours * morning_pay) + (after_school_pay * hours_after_school * 5) + (weekend_pay * hours_on_weekends)
    result = total_pay
    return result

print(solution())