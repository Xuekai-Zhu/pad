def solution():
    cups_per_hour_rose = 6
    cups_per_hour_lily = 7
    order_rose = 6
    order_lily = 14
    total_cups = order_rose + order_lily
    total_hours = (order_rose / cups_per_hour_rose) + (order_lily / cups_per_hour_lily)
    hourly_rate = 90 / total_hours
    result = hourly_rate
    return result

print(solution())