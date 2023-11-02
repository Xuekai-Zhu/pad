def solution():
    
    hourly_pay = 10
    first_year_raise = 0.2
    second_year_cut = 0.75
    new_hourly_pay = hourly_pay * (1 + first_year_raise)
    new_hourly_pay = new_hourly_pay * second_year_cut
    result = new_hourly_pay
    return result

print(solution())