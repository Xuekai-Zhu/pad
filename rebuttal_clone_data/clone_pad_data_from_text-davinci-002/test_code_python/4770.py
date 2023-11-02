def solution():
    hourly_rate_night = 1.50
    hourly_rate_morning = 2
    hours_stayed_night = 6
    hours_stayed_morning = 4
    total_cost = (hourly_rate_night * hours_stayed_night) + (hourly_rate_morning * hours_stayed_morning)
    money_left = 80 - total_cost
    result = money_left
    return result

print(solution())