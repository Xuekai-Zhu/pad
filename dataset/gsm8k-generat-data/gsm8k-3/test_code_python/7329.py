def solution():
    """Tara has a shoebox that is 4 inches tall and 6 inches wide. She puts a square block inside that is 4 inches per side. How many square inches of the box are left uncovered?"""
    # Calculate the area of the shoebox
    shoebox_area = 4 * 6

    # Calculate the area of the square block
    block_area = 4 ** 2

    # Calculate the area of the uncovered space
    uncovered_area = shoebox_area - block_area

    # Display the area of the uncovered space
    result = uncovered_area
    return result

print(solution())