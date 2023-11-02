def solution():
    """A 10 m long and 8 m wide rectangular floor is to be covered with a square carpet with 4 m sides. How many square meters of the floor are uncovered?"""
    # Calculate the area of the rectangular floor
    floor_area = 10 * 8

    # Calculate the area of the square carpet
    carpet_area = 4 * 4

    # Calculate the number of square meters of the floor that are uncovered
    uncovered_area = floor_area % carpet_area

    # Display the result
    result = uncovered_area
    return result

print(solution())