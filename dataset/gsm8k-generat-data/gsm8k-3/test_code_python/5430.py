def solution():
    """While practising for his upcoming math exams, Hayes realised that the area of a circle he had just solved was equal to the perimeter of a square he had solved in the previous problem.
    If the area of the circle was 100, what's the length of one side of the square?"""
    # Area of the circle is given by A = pi*r^2
    # Perimeter of the square is given by P = 4s, where s is the length of one side of the square

    import math
    
    # Area of the circle is given to be 100
    circle_area = 100
    
    # radius of the circle, using A = pi*r^2
    radius = math.sqrt(circle_area/math.pi)
    
    # perimeter of the square should be equal to the circumference of the circle  which is 2*pi*r
    square_perimeter = 2*math.pi*radius
    
    # length of one side of the square using P = 4s
    square_side = square_perimeter/4

    return square_side

print(solution())