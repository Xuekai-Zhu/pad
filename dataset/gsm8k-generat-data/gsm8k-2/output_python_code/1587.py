def solution():
    """Mary is making a model sailboat. She wants to add three sails: a rectangular sail that measures 5 inches by 8 inches and two right triangular sails, one that's 3 inches long at the bottom and 4 inches tall and one that's 4 inches long at the bottom and 6 inches tall. (Remember you can find the area of a triangle by dividing the area of a square with the same height and length by 2). How many square inches of canvas does she need total?"""
    rectangular_sail_area = 5 * 8
    triangle1_area = (3 * 4) / 2
    triangle2_area = (4 * 6) / 2
    total_area = rectangular_sail_area + triangle1_area + triangle2_area
    result = total_area
    return result

print(solution())