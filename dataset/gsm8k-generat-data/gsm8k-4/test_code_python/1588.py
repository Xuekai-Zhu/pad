def solution():
    """Mary is making a model sailboat. She wants to add three sails: a rectangular sail that measures 5 inches by 8 inches and two right triangular sails, one that's 3 inches long at the bottom and 4 inches tall and one that's 4 inches long at the bottom and 6 inches tall. How many square inches of canvas does she need total?"""
    # Calculate the area of the rectangular sail
    rectangular_sail_area = 5 * 8

    # Calculate the area of the first triangular sail
    first_triangular_sail_area = 0.5 * (3 * 4)

    # Calculate the area of the second triangular sail
    second_triangular_sail_area = 0.5 * (4 * 6)

    # Add the three areas to get the total area of canvas needed
    total_canvas_area = rectangular_sail_area + first_triangular_sail_area + second_triangular_sail_area

    # Return the result
    result = total_canvas_area
    return result

print(solution())