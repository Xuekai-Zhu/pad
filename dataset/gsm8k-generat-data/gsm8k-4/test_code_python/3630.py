def solution():
    """A construction company is building 2 apartment buildings with 12 floors each. The apartments are almost ready to sell but all of them need doors to be completed. Each floor has 6 apartments, and each apartment needs 7 doors in total. How many doors does the company need to buy?"""
    # Define the number of floors and apartments per building
    FLOORS_PER_BUILDING = 12
    APARTMENTS_PER_FLOOR = 6

    # Define the number of doors needed per apartment
    DOORS_PER_APARTMENT = 7

    # Calculate the total number of apartments per building
    total_apartments = FLOORS_PER_BUILDING * APARTMENTS_PER_FLOOR * 2

    # Calculate the total number of doors needed
    total_doors = total_apartments * DOORS_PER_APARTMENT

    # Return the result
    result = total_doors
    return result

print(solution())