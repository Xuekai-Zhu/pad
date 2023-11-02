def solution():
    """A particular train has some passenger cars and a number of cargo cars equal to half the number of passenger cars plus three.
    If the total number of cars is 71, counting the engine and caboose, how many passenger cars are in the train?"""
    # Define the total number of cars
    total_cars = 71 - 2 # Subtracting the engine and caboose

    # Calculate the number of cargo cars
    cargo_cars = (total_cars - 1) / 3 # Subtracting 1 passenger car for the engine

    # Calculate the number of passenger cars
    passenger_cars = total_cars - cargo_cars

    # Return the result
    result = passenger_cars
    return result

print(solution())