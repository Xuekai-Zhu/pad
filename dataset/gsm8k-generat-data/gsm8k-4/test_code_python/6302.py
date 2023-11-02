def solution():
    """Pauline has 125 matchbox cars. They are all either convertibles, trucks, regular cars. 64% of them are regular cars. 8% are trucks. How many convertibles does she own?"""
    # Define the total number of matchbox cars
    total_cars = 125

    # Calculate the number of regular cars
    regular_cars = total_cars * 0.64

    # Calculate the number of trucks
    trucks = total_cars * 0.08

    # Calculate the number of convertibles
    convertibles = total_cars - regular_cars - trucks

    # return the result
    result = convertibles
    return result

print(solution())