def solution():
    """Mary is making a model sailboat. She wants to add three sails: a rectangular sail that measures 5 inches by 8 inches and two right triangular sails, one that's 3 inches long at the bottom and 4 inches tall and one that's 4 inches long at the bottom and 6 inches tall.
    How many square inches of canvas does she need total?"""
    rect_sail_area = 5*8
    tri_sail_area_1 = (3*4)/2
    tri_sail_area_2 = (4*6)/2
    total_sail_area = rect_sail_area + tri_sail_area_1 + tri_sail_area_2
    result = total_sail_area
    return result

print(solution())