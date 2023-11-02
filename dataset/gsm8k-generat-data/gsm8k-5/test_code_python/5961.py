def solution():
    total_cars = 450  # Total number of cars that passed through the toll booth in a week
    monday_cars = 50  # Number of cars that passed through the toll booth on Monday
    tuesday_cars = monday_cars  # Number of cars that passed through the toll booth on Tuesday is the same as Monday
    wednesday_cars = 2 * monday_cars  # Number of cars that passed through the toll booth on Wednesday is double the number on Monday
    thursday_cars = 2 * monday_cars  # Number of cars that passed through the toll booth on Thursday is double the number on Monday
    remaining_cars = total_cars - monday_cars - tuesday_cars - wednesday_cars - thursday_cars  # Remaining number of cars

    # Calculate the total number of cars that passed through the toll booth on each of the remaining days
    remaining_days_cars = remaining_cars / 3

    result = remaining_days_cars
    return result

print(solution())