def solution():
    cathy_cars = 5  # Cathy owns 5 cars
    lindsey_cars = cathy_cars + 4  # Lindsey owns 4 more cars than Cathy
    carol_cars = cathy_cars * 2  # Carol owns twice as many cars as Cathy
    susan_cars = carol_cars - 2  # Susan owns 2 fewer cars than Carol

    # Calculate the total number of cars owned by all four women
    total_cars = cathy_cars + lindsey_cars + carol_cars + susan_cars
    result = total_cars
    return result

print(solution())