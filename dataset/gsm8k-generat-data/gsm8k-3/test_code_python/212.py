def solution():
    """Bobby has 16 toy cars, and the number of cars he has increases by 50% every year. How many toy cars will Bobby have in three years?"""
    # Define the initial number of toy cars
    initial_cars = 16

    # Define the percentage increase each year
    yearly_increase = 0.5

    # Calculate the number of cars Bobby will have in three years
    cars_in_three_years = initial_cars * (1 + yearly_increase) ** 3

    # Display the number of cars Bobby will have in three years
    result = cars_in_three_years
    return result

print(solution())