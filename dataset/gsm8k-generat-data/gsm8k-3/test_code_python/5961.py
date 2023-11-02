def solution():
    """In a week, 450 cars drove through a toll booth. Fifty vehicles went through the toll booth on Monday and the same number of vehicles drove through the toll booth on Tuesday. On each of Wednesday and Thursday, twice the number of cars that passed through the toll booth on Monday went through the toll booth. If, for the remaining of the days of the week, an equal number of vehicles passed through the toll booth, calculate the total number of cars that passed the toll both in each of the remaining days."""
    # Calculate the number of cars that passed through the toll booth on Monday and Tuesday
    monday_cars = 50
    tuesday_cars = monday_cars

    # Calculate the number of cars that passed through the toll booth on Wednesday and Thursday
    wednesday_cars = monday_cars * 2
    thursday_cars = wednesday_cars

    # Calculate the total number of cars that passed through the toll booth on Monday through Thursday
    first_four_days_cars = monday_cars + tuesday_cars + wednesday_cars + thursday_cars

    # Calculate the number of cars that passed through the toll booth on the remaining days
    remaining_days_cars = 450 - first_four_days_cars

    # Calculate the total number of cars that passed through the toll booth on each of the remaining days
    each_remaining_day_cars = remaining_days_cars / 3

    # Display the total number of cars that passed through the toll booth on each of the remaining days
    result = each_remaining_day_cars
    return result

print(solution())