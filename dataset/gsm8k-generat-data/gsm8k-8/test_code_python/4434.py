def solution():
    # Define the number of theme parks in Jamestown
    jamestown_parks = 20

    # Calculate the number of parks in Venice and Marina Del Ray
    venice_parks = jamestown_parks + 25
    marina_parks = jamestown_parks + 50

    # Calculate the total number of parks in the three towns
    total_parks = jamestown_parks + venice_parks + marina_parks

    result = total_parks
    return result

print(solution())