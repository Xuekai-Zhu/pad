def solution():
    upfront_cost = 1000
    court_time_hours = 50
    prep_time_hours = 2 * court_time_hours
    hourly_rate = 100
    total_hours = court_time_hours + prep_time_hours
    total_cost = upfront_cost + (total_hours * hourly_rate)
    john_paid = total_cost / 2
    result = john_paid
    return result

print(solution())