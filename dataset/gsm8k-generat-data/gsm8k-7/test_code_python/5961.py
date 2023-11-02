def solution():
    total_cars = 450
    monday_cars = 50
    tuesday_cars = monday_cars
    wednesday_cars = 2 * monday_cars
    thursday_cars = 2 * monday_cars
    remaining_cars = total_cars - monday_cars - tuesday_cars - wednesday_cars - thursday_cars

    # Calculate the number of cars that passed the toll booth on each of the remaining days
    remaining_cars_per_day = remaining_cars / 3

    result = remaining_cars_per_day
    return result

print(solution())