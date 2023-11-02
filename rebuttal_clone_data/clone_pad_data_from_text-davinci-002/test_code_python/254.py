def solution():
    """Nate got lost looking for his car in the airport parking lot. He had to walk through every row in Section G and Section H to find it. Section G has 15 rows that each hold 10 cars. Section H has 20 rows that each hold 9 cars. If Nate can walk past 11 cars per minute, how many minutes did he spend searching the parking lot?"""
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