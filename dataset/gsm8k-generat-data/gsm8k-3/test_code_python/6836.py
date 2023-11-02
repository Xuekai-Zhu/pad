def solution():
    """Darius, Matt, and Marius are friends, who played table football. During all the games they played, Marius scored 3 points more than Darius, and Darius scored 5 points less than Matt. How many points did all three friends score together, if Darius scored 10 points?"""
    # Define the number of points scored by Darius
    darius_points = 10

    # Calculate the number of points scored by Matt and Marius
    matt_points = darius_points + 5
    marius_points = darius_points + 3

    # Calculate the total number of points scored by all three friends
    total_points = darius_points + matt_points + marius_points

    # Display the total number of points scored
    result = total_points
    return result

print(solution())