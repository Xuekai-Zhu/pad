def solution():
    """Lindsey owns 4 more cars than Cathy. Susan owns 2 fewer cars than Carol. Carol owns twice as many cars as Cathy. If Cathy owns 5 cars, how many total cars do they all own put together?"""
    cathy_cars = 5
    lindsey_cars = cathy_cars + 4
    carol_cars = 2 * cathy_cars
    susan_cars = carol_cars - 2
    total_cars = cathy_cars + lindsey_cars + carol_cars + susan_cars
    result = total_cars
    return result

print(solution())