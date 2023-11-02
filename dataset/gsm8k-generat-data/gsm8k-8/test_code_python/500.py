def solution():
    # Define the total number of catches
    total_catches = 23

    # Calculate Derek's number of catches
    derek_catches = 2 * total_catches - 4

    # Calculate Tammy's number of catches
    tammy_catches = (1/3) * derek_catches + 16

    result = tammy_catches
    return result

print(solution())