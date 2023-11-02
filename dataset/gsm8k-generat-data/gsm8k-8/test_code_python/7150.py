def solution():
    # Calculate the number of cars Lindsey owns
    cathy_cars = 5
    lindsey_cars = cathy_cars + 4

    # Calculate the number of cars Carol owns
    carol_cars = 2 * cathy_cars

    # Calculate the number of cars Susan owns
    susan_cars = carol_cars - 2

    # Calculate the total number of cars they all own
    total_cars = cathy_cars + lindsey_cars + carol_cars + susan_cars

    result = total_cars
    return result

print(solution())