def solution():
    """Gerald had 20 toy cars. He donated 1/4 of his toy cars to an orphanage. How many toy cars does Gerald have left?"""
    # Define the initial number of toy cars
    initial_cars = 20

    # Calculate the number of toy cars donated to the orphanage
    donated_cars = initial_cars / 4

    # Calculate the number of toy cars left with Gerald
    remaining_cars = initial_cars - donated_cars

    # return the result
    result = remaining_cars
    return result

print(solution())