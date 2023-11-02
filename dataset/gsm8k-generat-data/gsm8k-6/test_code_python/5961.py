def solution():
    # Calculate the number of cars that passed the toll booth on Monday and Tuesday
    monday_cars = 50
    tuesday_cars = monday_cars
    total_cars = 450

    # Calculate the number of cars that passed the toll booth on Wednesday and Thursday
    wednesday_cars = 2 * monday_cars
    thursday_cars = 2 * monday_cars

    # Calculate the remaining number of cars
    remaining_cars = total_cars - monday_cars - tuesday_cars - wednesday_cars - thursday_cars

    # Calculate the number of cars that passed the toll booth on each of the remaining days
    remaining_days_cars = remaining_cars // 3

    # Calculate the total number of cars that passed the toll booth in each of the remaining days
    result = remaining_days_cars
    return result

print(solution())