def solution():
    
    cars_per_row_G = 10
    cars_per_row_H = 9
    rows_G = 15
    rows_H = 20
    total_cars = cars_per_row_G * rows_G + cars_per_row_H * rows_H
    cars_per_minute = 11
    minutes_spent = total_cars / cars_per_minute
    result = minutes_spent
    return result

print(solution())