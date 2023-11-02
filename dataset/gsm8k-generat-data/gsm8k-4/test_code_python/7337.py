def solution():
    """A road has four intersections. At the first intersection, there are 40 road signs showing different types of information mounted on the street poles. At the second intersection, 1/4 times more road signs than the first intersection are mounted on the street poles. The number of road signs at the third intersection is twice the number at the second intersection. If at the fourth intersection the number of road signs is 20 fewer than those at the third intersection, calculate the total number of road signs at the four intersections."""
    # Define the number of road signs at the first intersection
    intersection_1 = 40

    # Calculate the number of road signs at the second intersection
    intersection_2 = intersection_1 + (1/4 * intersection_1)

    # Calculate the number of road signs at the third intersection
    intersection_3 = intersection_2 * 2

    # Calculate the number of road signs at the fourth intersection
    intersection_4 = intersection_3 - 20

    # Calculate the total number of road signs at all four intersections
    total_signs = intersection_1 + intersection_2 + intersection_3 + intersection_4

    # return the result
    result = total_signs
    return result

print(solution())