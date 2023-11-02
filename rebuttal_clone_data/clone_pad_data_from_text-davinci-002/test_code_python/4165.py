def solution():
    days = 6
    sandwiches_per_day = 2
    for day in range(1, days+1):
        if day % 3 == 1:
            sandwiches_per_day = 2
        elif day % 3 == 2:
            sandwiches_per_day = sandwiches_per_day*2
        elif day % 3 == 0:
            sandwiches_per_day = sandwiches_per_day*2
    result = sandwiches_per_day
    return result

print(solution())