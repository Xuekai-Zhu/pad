def solution():
    """Nate got lost looking for his car in the airport parking lot. He had to walk through every row in Section G and Section H to find it. Section G has 15 rows that each hold 10 cars. Section H has 20 rows that each hold 9 cars. If Nate can walk past 11 cars per minute, how many minutes did he spend searching the parking lot?"""
    # Calculate the number of cars in Section G
    g_cars = 15 * 10

    # Calculate the number of cars in Section H
    h_cars = 20 * 9

    # Calculate the total number of cars in both sections
    total_cars = g_cars + h_cars

    # Calculate the time it takes to walk past one car
    time_per_car = 1 / 11

    # Calculate the total time spent searching for his car
    total_time = total_cars * time_per_car

    # Display the total time
    result = total_time
    return result

print(solution())