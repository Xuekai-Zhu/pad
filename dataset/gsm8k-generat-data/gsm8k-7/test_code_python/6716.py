def solution():
    # Area of one square = 4*4 = 16 sq. inches
    area_of_one_square = 16

    # Each marker can color 3 squares, so each square uses 1/3 of the ink
    ink_per_square = 1/3

    # Area of one rectangle = 6*2 = 12 sq. inches
    area_of_one_rectangle = 12

    # Area of two rectangles = 24 sq. inches
    area_of_two_rectangles = 24

    # Total area colored = area of squares + area of rectangles
    total_area_colored = area_of_two_rectangles + (3 * area_of_one_square)

    # Total ink used = total area colored * ink per square
    total_ink_used = total_area_colored * ink_per_square

    # Percentage of ink left = 100% - (ink used/total ink) * 100%
    percentage_of_ink_left = 100 - ((total_ink_used / (3 * ink_per_square)) * 100)

    result = percentage_of_ink_left
    return result

print(solution())