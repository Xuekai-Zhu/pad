def solution():
    """In Mariam's neighborhood, there are 40 houses on one side of the main road passing through the neighborhood and three times as many homes on the other side of the road. How many homes are in Mariam's neighborhood?"""
    # Define the number of houses on one side of the road
    houses_one_side = 40

    # Calculate the number of houses on the other side of the road
    houses_other_side = houses_one_side * 3

    # Calculate the total number of houses in the neighborhood
    total_houses = houses_one_side + houses_other_side

    # Display the total number of houses
    result = total_houses
    return result

print(solution())