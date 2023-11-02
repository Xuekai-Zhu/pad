def solution():
    months = [3, 4, 9, 10]
    frequency = 2
    total_gallons = 0
    for month in months:
        total_gallons += frequency * 2
    months = [5, 6, 7, 8]
    frequency = 4
    for month in months:
        total_gallons += frequency * 2
    result = total_gallons
    return result

print(solution())