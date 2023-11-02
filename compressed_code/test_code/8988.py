def solution():
    
    upfront_cost = 1000
    hourly_cost = 100
    court_time = 50
    prep_time = court_time * 2
    total_hours = court_time + prep_time
    total_cost = upfront_cost + (total_hours * hourly_cost)
    john_share = total_cost / 2
    result = john_share
    return result

print(solution())