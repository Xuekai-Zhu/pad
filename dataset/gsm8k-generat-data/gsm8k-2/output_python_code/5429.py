def solution():
    """While practising for his upcoming math exams, Hayes realised that the area of a circle he had just solved was equal to the perimeter of a square he had solved in the previous problem. If the area of the circle was 100, what's the length of one side of the square?"""
    circle_area = 100
    circle_radius = (circle_area / 3.14) ** 0.5
    square_perimeter = 2 * circle_radius * 3.14
    square_side_length = square_perimeter / 4
    result = square_side_length
    return result

print(solution())