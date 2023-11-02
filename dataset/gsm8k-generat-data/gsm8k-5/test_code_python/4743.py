def solution():
    tires_per_motorcycle = 2  # Each motorcycle has 2 tires
    tires_per_car = 4  # Each car has 4 tires

    # Calculate the total number of motorcycle tires
    motorcycle_tires = tires_per_motorcycle * 12

    # Calculate the total number of car tires
    car_tires = tires_per_car * 10

    # Calculate the total number of tires changed
    total_tires = motorcycle_tires + car_tires
    result = total_tires
    return result

print(solution())