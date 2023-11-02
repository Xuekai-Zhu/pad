def solution():
    """Mary is making a model sailboat. She wants to add three sails: a rectangular sail that measures 5 inches by 8 inches and two right triangular sails, one that's 3 inches long at the bottom and 4 inches tall and one that's 4 inches long at the bottom and 6 inches tall.
    (Remember you can find the area of a triangle by dividing the area of a square with the same height and length by 2).
    How many square inches of canvas does she need total?"""
    
    # Calculate the area of the rectangular sail
    rectangle_area = 5 * 8

    # Calculate the area of the first triangular sail
    triangle_area_1 = 0.5 * (4 * 3) # 0.5 * base * height

    # Calculate the area of the second triangular sail
    triangle_area_2 = 0.5 * (6 * 4) # 0.5 * base * height

    # Calculate the total area of canvas needed
    total_area = rectangle_area + triangle_area_1 + triangle_area_2

    # Display the total area
    result = total_area
    return result

print(solution())