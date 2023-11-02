def solution():
    
    pills_per_day = 1
    total_pills = 0
    for i in range(7):
        total_pills += pills_per_day
        pills_per_day += 2

    result = total_pills
    return result

print(solution())