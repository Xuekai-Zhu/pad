def solution():
    wallace_gallons = 40
    wallace_percent = 3/4
    wallace_capacity = wallace_gallons * wallace_percent
    catherine_gallons = wallace_gallons / 2
    catherine_percent = 3/4
    catherine_capacity = catherine_gallons * catherine_percent
    total_gallons = wallace_capacity + catherine_capacity
    result = total_gallons
    return result

print(solution())