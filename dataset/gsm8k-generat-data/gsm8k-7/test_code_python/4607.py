def solution():
    initial_rate = 40  # pages per hour
    weekly_total = 600  # pages
    new_rate = initial_rate * 1.5  # 150% increase
    new_hours = (weekly_total / new_rate) - 4  # four fewer hours per week
    new_total = new_rate * new_hours
    result = new_total
    return result

print(solution())