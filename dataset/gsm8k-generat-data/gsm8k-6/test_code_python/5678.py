def solution():
    total_cars = 71  # total number of cars in the train
    cargo_cars = (total_cars - 2) / 2  # number of cargo cars is half the number of passenger cars plus three
    passenger_cars = total_cars - cargo_cars - 2  # subtract engine and caboose from total cars
    result = passenger_cars
    return result

print(solution())