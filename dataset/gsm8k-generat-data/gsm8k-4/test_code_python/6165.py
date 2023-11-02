def solution():
    """Tamtam collected 65 shells in total. She got 13 purple shells, 8 pink shells, 18 yellow shells, and 12 blue shells. The remaining shells are color orange. How many orange shells are there?"""
    # Define the total number of shells collected
    total_shells = 65

    # Calculate the number of shells of each color
    purple_shells = 13
    pink_shells = 8
    yellow_shells = 18
    blue_shells = 12

    # Calculate the total number of shells of known colors
    known_shells = purple_shells + pink_shells + yellow_shells + blue_shells

    # Calculate the number of orange shells
    orange_shells = total_shells - known_shells

    # Return the result
    result = orange_shells
    return result

print(solution())