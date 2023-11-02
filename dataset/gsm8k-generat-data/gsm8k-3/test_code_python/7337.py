def solution():
    """A road has four intersections. At the first intersection, there are 40 road signs showing different types of information mounted on the street poles. At the second intersection, 1/4 times more road signs than the first intersection are mounted on the street poles. The number of road signs at the third intersection is twice the number at the second intersection. If at the fourth intersection the number of road signs is 20 fewer than those at the third intersection, calculate the total number of road signs at the four intersections."""
    # Calculate the number of road signs at the second intersection
    signs_2 = 40 * (1 + 1/4)

    # Calculate the number of road signs at the third intersection
    signs_3 = 2 * signs_2

    # Calculate the number of road signs at the fourth intersection
    signs_4 = signs_3 - 20

    # Calculate the total number of road signs at all four intersections
    total_signs = 40 + signs_2 + signs_3 + signs_4

    # Display the total number of road signs
    result = total_signs
    return result

print(solution())