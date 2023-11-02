def solution():
    upfront_pay = 1000
    hourly_pay = 100
    court_time = 50
    prep_time = court_time * 2
    total_hours = court_time + prep_time
    total_pay = upfront_pay + (hourly_pay * total_hours)
    brother_pay = total_pay / 2
    john_pay = total_pay - brother_pay
    result = john_pay
    
    return result

print(solution())