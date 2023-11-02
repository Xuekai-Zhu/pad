def solution():
    # Calculate the area of the quilt
    quilt_area = 6 * 24

    # Calculate the diagonal of the square
    square_diagonal = (2 * quilt_area)**0.5

    # Calculate the length of each side of the square using Pythagorean theorem
    square_side = (square_diagonal**2 / 2)**0.5

    result = square_side
    return result

print(solution())