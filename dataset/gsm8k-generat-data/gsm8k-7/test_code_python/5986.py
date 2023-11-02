def solution():
    tuition_cost = 22000
    parents_payment = tuition_cost / 2
    scholarship = 3000
    loan = scholarship * 2
    total_available_funds = parents_payment + scholarship + loan
    hours_worked = 200
    remaining_tuition = tuition_cost - total_available_funds
    hourly_rate = remaining_tuition / hours_worked
    result = hourly_rate
    return result

print(solution())