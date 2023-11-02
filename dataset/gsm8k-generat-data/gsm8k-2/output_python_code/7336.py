def solution():
    """A road has four intersections. At the first intersection, there are 40 road signs showing different types of information mounted on the street poles. At the second intersection, 1/4 times more road signs than the first intersection are mounted on the street poles. The number of road signs at the third intersection is twice the number at the second intersection. If at the fourth intersection the number of road signs is 20 fewer than those at the third intersection, calculate the total number of road signs at the four intersections."""
    intersection_1 = 40
    intersection_2 = int(intersection_1 * 1.25)
    intersection_3 = intersection_2 * 2
    intersection_4 = intersection_3 - 20
    total_signs = intersection_1 + intersection_2 + intersection_3 + intersection_4
    result = total_signs
    return result

print(solution())