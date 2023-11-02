def solution():
    # Calculate the number of cars owned by Lindsey, Cathy, and Carol
    cathy_cars = 5
    carol_cars = 2 * cathy_cars
    lindsey_cars = cathy_cars + 4

    # Calculate the number of cars owned by Susan
    susan_cars = carol_cars - 2

    # Calculate the total number of cars owned by all of them
    total_cars = cathy_cars + carol_cars + lindsey_cars + susan_cars
    result = total_cars
    return result

print(solution())