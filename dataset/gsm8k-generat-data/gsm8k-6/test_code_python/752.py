def solution():
    area = 100  # given area of the rectangle
    # Let's assume width as w, then length will be 4w
    width = ((area/4)**0.5)  # Calculate the width of the rectangle
    length = 4 * width  # Calculate the length of the rectangle
    result = length
    return result

print(solution())