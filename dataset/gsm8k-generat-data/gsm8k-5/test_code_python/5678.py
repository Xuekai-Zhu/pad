def solution():
    total_cars = 71  # Total number of cars, including engine and caboose
    cargo_cars = (total_cars - 2) // 3  # Number of cargo cars is half the number of passenger cars plus three
    passenger_cars = total_cars - 2 - cargo_cars  # Number of passenger cars is total number of cars minus engine, caboose, and cargo cars
    result = passenger_cars
    return result

print(solution())