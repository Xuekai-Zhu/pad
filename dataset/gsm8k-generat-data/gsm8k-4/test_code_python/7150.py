def solution():
    """Lindsey owns 4 more cars than Cathy. Susan owns 2 fewer cars than Carol. Carol owns twice as many cars as Cathy. If Cathy owns 5 cars, how many total cars do they all own put together?"""
    # Define the number of cars that Cathy owns
    cathy_cars = 5

    # Calculate the number of cars that Lindsey owns
    lindsey_cars = cathy_cars + 4

    # Calculate the number of cars that Carol owns
    carol_cars = 2 * cathy_cars

    # Calculate the number of cars that Susan owns
    susan_cars = carol_cars - 2

    # Calculate the total number of cars owned by all of them
    total_cars = cathy_cars + lindsey_cars + carol_cars + susan_cars

    result = total_cars
    return result

print(solution())