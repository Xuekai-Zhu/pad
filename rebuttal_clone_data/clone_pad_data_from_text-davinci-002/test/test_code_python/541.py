def solution():
    requests_per_day = 6
    requests_worked_on_per_day = 4
    requests_remaining = requests_per_day - requests_worked_on_per_day
    result = requests_remaining * 5
    return result

print(solution())