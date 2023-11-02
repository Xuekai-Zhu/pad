def solution():
    cathy_cars = 5
    lindsey_cars = cathy_cars + 4
    carol_cars = cathy_cars * 2
    susan_cars = carol_cars - 2

    # Calculate the total number of cars owned by all four people
    total_cars = cathy_cars + lindsey_cars + carol_cars + susan_cars
    result = total_cars
    return result

print(solution())