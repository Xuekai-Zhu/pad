def solution():
    """Lindsey owns 4 more cars than Cathy. Susan owns 2 fewer cars than Carol. Carol owns twice as many cars as Cathy. If Cathy owns 5 cars, how many total cars do they all own put together?"""
    # Calculate the number of cars owned by Cathy
    cathy_cars = 5

    # Calculate the number of cars owned by Carol
    carol_cars = cathy_cars * 2

    # Calculate the number of cars owned by Lindsey
    lindsey_cars = cathy_cars + 4

    # Calculate the number of cars owned by Susan
    susan_cars = carol_cars - 2

    # Calculate the total number of cars owned by all of them
    total_cars = cathy_cars + carol_cars + lindsey_cars + susan_cars

    # Display the total number of cars
    result = total_cars
    return result

print(solution())