def solution():
    """In a week, 450 cars drove through a toll booth. Fifty vehicles went through the toll booth on Monday and the same number of vehicles drove through the toll booth on Tuesday. On each of Wednesday and Thursday, twice the number of cars that passed through the toll booth on Monday went through the toll booth. If, for the remaining of the days of the week, an equal number of vehicles passed through the toll booth, calculate the total number of cars that passed the toll both in each of the remaining days."""
    total_cars = 450
    monday_cars = 50
    tuesday_cars = monday_cars
    wednesday_cars = 2 * monday_cars
    thursday_cars = 2 * monday_cars
    remaining_cars = total_cars - monday_cars - tuesday_cars - wednesday_cars - thursday_cars
    remaining_days = 7 - 4
    other_cars_per_day = remaining_cars // remaining_days
    result = other_cars_per_day
    return result

print(solution())