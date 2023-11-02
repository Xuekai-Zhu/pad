def solution():
    
    starting_amount = 20
    weekly_contrib = 10
    vacuum_price = 120
    weeks_needed = (vacuum_price - starting_amount) / weekly_contrib
    result = weeks_needed
    return result

print(solution())