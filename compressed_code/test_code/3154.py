def solution():
    
    upfront_payment = 1000
    hourly_rate = 100
    court_time = 50
    prep_time = court_time * 2
    total_hours = court_time + prep_time
    total_cost = upfront_payment + (total_hours * hourly_rate)
    john_share = total_cost * 0.5
    result = john_share
    return result

print(solution())