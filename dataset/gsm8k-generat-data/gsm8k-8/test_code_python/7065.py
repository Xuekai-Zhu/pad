def solution():
    # Define the number of vehicles Juan saw
    cars = 15
    bicycles = 3
    trucks = 8
    tricycle = 1

    # Calculate the total number of tires on the vehicles
    total_tires = cars * 4 + bicycles * 2 + trucks * 4 + tricycle * 3
    result = total_tires
    return result

print(solution())