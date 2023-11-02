def solution():
    perimeter = 30 # Perimeter of the sandbox is 30 feet
    length = 2 * width # Length is twice the width
    # Let's assume width is 'w'
    # Perimeter of a rectangle is 2(length + width)
    # Therefore, 2(length + w) = 30
    # Substituting length as 2w, we get 2(2w + w) = 30
    # Solving the equation, we get w = 5 (width of the sandbox)
    width = 5
    result = width
    return result

print(solution())