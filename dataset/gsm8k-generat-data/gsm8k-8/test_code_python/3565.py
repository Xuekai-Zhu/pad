def solution():
    # Let's assume the width of the patio as x
    width = x

    # According to the problem, length of the patio is 4 times its width
    length = 4*x

    # Perimeter of the patio is 100 feet
    perimeter = 2*(length + width)

    # We can simplify the perimeter equation as follows
    100 = 2*(4x + x)
    100 = 10x
    x = 10 # width is 10 feet

    # Length of the patio can be calculated as
    length = 4*x
    result = length
    return result

print(solution())