def solution():
    """A 10 m long and 8 m wide rectangular floor is to be covered with a square carpet with 4 m sides. How many square meters of the floor are uncovered?"""
    # Define the dimensions of the floor and carpet
    floor_length = 10
    floor_width = 8
    carpet_side = 4

    # Calculate the area of the floor and carpet
    floor_area = floor_length * floor_width
    carpet_area = carpet_side ** 2

    # Calculate the number of squares needed to cover the floor
    num_squares = floor_area // carpet_area

    # Calculate the area of the uncovered portion of the floor
    uncovered_area = floor_area - (num_squares * carpet_area)

    # return the result
    result = uncovered_area
    return result

print(solution())