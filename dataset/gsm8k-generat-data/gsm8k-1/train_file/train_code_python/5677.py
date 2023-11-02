def solution():
    """A particular train has some passenger cars and a number of cargo cars equal to half the number of passenger cars
    plus three. If the total number of cars is 71, counting the engine and caboose, how many passenger cars are in the
    train?"""
    total_cars = 71
    cargo_cars = (total_cars - 2) / 2
    passenger_cars = total_cars - cargo_cars - 2
    result = passenger_cars
    return result

print(solution())