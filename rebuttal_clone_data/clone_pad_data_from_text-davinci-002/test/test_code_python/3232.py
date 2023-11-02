def solution():
    cost_ticket = 11
    cost_drinks = 3
    cost_headphones = 16
    cost_wifi = 2
    hourly_earnings = 12
    total_cost = cost_ticket + cost_drinks + cost_headphones + cost_wifi
    break_even_time = total_cost / hourly_earnings
    result = break_even_time
    return result

print(solution())