def solution():
    
    initial_pollywogs = 2400
    matured_pollywogs_rate = 50
    melvin_daily_catch = 10
    days_with_melvin = 20
    total_matured_pollywogs = 0
    days = 0

    while initial_pollywogs > 0:
        initial_pollywogs -= matured_pollywogs_rate
        total_matured_pollywogs += matured_pollywogs_rate

        if days <= days_with_melvin:
            initial_pollywogs -= melvin_daily_catch

        days += 1

    result = days
    return result

print(solution())