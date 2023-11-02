def solution():
    hourly_wage = 10
    application_fee = 25
    number_of_colleges = 6
    total_fees = application_fee * number_of_colleges
    total_hours = total_fees / hourly_wage
    result = total_hours
    return result

print(solution())