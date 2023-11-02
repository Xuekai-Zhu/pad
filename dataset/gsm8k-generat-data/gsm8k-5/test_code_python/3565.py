def solution():
    # Let's assume the width of the patio to be 'x'
    width = x
    length = 4 * x  # Length is four times the width

    perimeter = 100  # Perimeter is given as 100 feet
    # Perimeter = 2*(length+width), substituting the values, we get:
    2 * (length + width) = 100
    2 * (4x + x) = 100
    10x = 100
    x = 10  # Width is 10 feet

    # Length is four times the width, i.e. 4*10=40
    length = 40

    result = length
    return result

print(solution())