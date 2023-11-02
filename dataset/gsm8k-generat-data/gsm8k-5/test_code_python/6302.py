def solution():
    total_cars = 125  # Pauline has 125 matchbox cars
    regular_cars_percentage = 64  # 64% of the cars are regular cars
    trucks_percentage = 8  # 8% of the cars are trucks

    # Calculate the number of regular cars
    regular_cars = int(total_cars * regular_cars_percentage / 100)

    # Calculate the number of trucks
    trucks = int(total_cars * trucks_percentage / 100)

    # Calculate the number of convertibles
    convertibles = total_cars - regular_cars - trucks
    result = convertibles
    return result

print(solution())