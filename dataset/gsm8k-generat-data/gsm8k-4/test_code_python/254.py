def solution():
    """Nate got lost looking for his car in the airport parking lot. He had to walk through every row in Section G and Section H to find it. Section G has 15 rows that each hold 10 cars. Section H has 20 rows that each hold 9 cars. If Nate can walk past 11 cars per minute, how many minutes did he spend searching the parking lot?"""
    # Define the number of rows and cars in each section
    rows_G = 15
    cars_row_G = 10
    rows_H = 20
    cars_row_H = 9

    # Calculate the total number of cars in each section
    total_cars_G = rows_G * cars_row_G
    total_cars_H = rows_H * cars_row_H

    # Calculate the total number of cars Nate walked past
    total_cars_walked = total_cars_G + total_cars_H

    # Calculate the time spent walking past cars
    time_spent = total_cars_walked / 11

    # return the result
    result = time_spent
    return result

print(solution())