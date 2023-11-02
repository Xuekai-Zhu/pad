def solution():
    """Gerald had 20 toy cars. He donated 1/4 of his toy cars to an orphanage. How many toy cars does Gerald have left?"""
    # Define the initial number of toy cars
    initial_num_cars = 20

    # Calculate the number of cars donated
    num_cars_donated = initial_num_cars / 4

    # Calculate the number of cars left
    num_cars_left = initial_num_cars - num_cars_donated

    # Display the number of cars left
    result = num_cars_left
    return result

print(solution())