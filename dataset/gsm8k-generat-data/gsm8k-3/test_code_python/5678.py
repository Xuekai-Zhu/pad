def solution():
    """A particular train has some passenger cars and a number of cargo cars equal to half the number of passenger cars plus three. If the total number of cars is 71, counting the engine and caboose, how many passenger cars are in the train?"""
    # Define the number of cargo cars in terms of the number of passenger cars
    cargo_cars = 0.5 * passenger_cars + 3

    # Define the total number of cars in terms of the number of passenger cars
    total_cars = passenger_cars + cargo_cars + 2  # add 2 for the engine and caboose

    # Set up an equation for the total number of cars
    # passenger_cars + cargo_cars + 2 = 71
    # substitute cargo_cars = 0.5 * passenger_cars + 3
    # passenger_cars + (0.5 * passenger_cars + 3) + 2 = 71
    # distribute the 0.5 and simplify
    # 1.5 * passenger_cars + 5 = 71
    # subtract 5 from both sides
    # 1.5 * passenger_cars = 66
    # divide by 1.5
    # passenger_cars = 44

    # Calculate the number of passenger cars
    passenger_cars = 44

    # Display the number of passenger cars
    result = passenger_cars
    return result

print(solution())