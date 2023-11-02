def solution():
    allowance_1 = 50
    allowance_2 = 0
    job_pay = 9
    hours_worked = 30
    weekly_spending = 35
    car_cost = 15000
    total_saved_1 = allowance_1 * 52
    total_saved_2 = (job_pay * hours_worked * 52) - (weekly_spending * 52)
    total_saved = total_saved_1 + total_saved_2
    needed = car_cost - total_saved
    result = needed
    return result

print(solution())