def solution():
    """In a week, 450 cars drove through a toll booth. Fifty vehicles went through the toll booth on Monday and the same number of vehicles drove through the toll booth on Tuesday. On each of Wednesday and Thursday, twice the number of cars that passed through the toll booth on Monday went through the toll booth. If, for the remaining of the days of the week, an equal number of vehicles passed through the toll booth, calculate the total number of cars that passed the toll both in each of the remaining days."""
    # Define the number of cars that passed through the toll booth on Monday and Tuesday
    monday_cars = 50
    tuesday_cars = monday_cars

    # Define the number of cars that passed through the toll booth on Wednesday and Thursday
    wednesday_cars = 2 * monday_cars
    thursday_cars = wednesday_cars

    # Calculate the total number of cars that passed through the toll booth on Monday to Thursday
    total_cars = monday_cars + tuesday_cars + wednesday_cars + thursday_cars

    # Calculate the number of cars that passed through the toll booth on each of the remaining days of the week
    remaining_days = 7 - 4
    remaining_cars = (450 - total_cars) / remaining_days

    # return the result
    result = remaining_cars
    return result

print(solution())