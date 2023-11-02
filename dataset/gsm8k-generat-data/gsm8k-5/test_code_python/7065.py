def solution():
    cars = 15
    bicycles = 3
    pickup_trucks = 8
    tricycles = 1

    # Calculate the total number of tires on the vehicles Juan saw
    total_tires = (cars * 4) + (bicycles * 2) + (pickup_trucks * 4) + (tricycles * 3)
    result = total_tires
    return result

print(solution())