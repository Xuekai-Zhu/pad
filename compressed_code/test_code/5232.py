def solution():
    
    total_cars = 3000
    less_than_15000_percent = 0.15
    more_than_20000_percent = 0.4

    less_than_15000 = total_cars * less_than_15000_percent
    more_than_20000 = total_cars * more_than_20000_percent
    between_15000_and_20000 = total_cars - less_than_15000 - more_than_20000

    result = between_15000_and_20000
    return result

print(solution())