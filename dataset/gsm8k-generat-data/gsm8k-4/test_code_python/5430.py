def solution():
    """While practising for his upcoming math exams, Hayes realised that the area of a circle he had just solved was equal to the perimeter of a square he had solved in the previous problem. If the area of the circle was 100, what's the length of one side of the square?"""
    # Define the area of the circle
    area_circle = 100

    # Calculate the radius of the circle
    radius_circle = (area_circle / 3.14) ** 0.5

    # Calculate the perimeter of the square
    perimeter_square = 4 * (radius_circle ** 2)

    # Calculate the length of one side of the square
    length_square = perimeter_square / 4

    result = length_square
    return result

print(solution())