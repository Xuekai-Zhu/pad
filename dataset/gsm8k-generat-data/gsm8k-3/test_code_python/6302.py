def solution():
    """Pauline has 125 matchbox cars. They are all either convertibles, trucks, regular cars. 64% of them are regular cars. 8% are trucks. How many convertibles does she own?"""
    # Define the total number of matchbox cars Pauline owns
    total_cars = 125

    # Calculate the number of regular cars she owns
    regular_cars = int(total_cars * 0.64)

    # Calculate the number of trucks she owns
    trucks = int(total_cars * 0.08)

    # Calculate the number of convertibles she owns
    convertibles = total_cars - regular_cars - trucks

    # Display the number of convertibles she owns
    result = convertibles
    return result

print(solution())