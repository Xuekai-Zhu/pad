def solution():
    # Define the total number of cars
    total_cars = 125

    # Calculate the number of regular cars and trucks
    regular_cars = total_cars * 0.64
    trucks = total_cars * 0.08

    # Calculate the number of convertibles
    convertibles = total_cars - regular_cars - trucks
    result = convertibles
    return result

print(solution())