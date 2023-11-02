def solution():
    initial_population = 80000
    daily_loss = 1200
    threshold_population = initial_population / 4

    days = 0
    current_population = initial_population
    while current_population > threshold_population:
        current_population -= daily_loss
        days += 1

    result = days
    return result

print(solution())