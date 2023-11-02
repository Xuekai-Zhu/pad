def solution():
    # Calculate the total area of the three squares
    area1 = 8 * 5
    area2 = 10 * 7
    area3 = 5 * 5
    total_area = area1 + area2 + area3

    # Calculate the width of the flag
    width = total_area / 15

    # Calculate the height of the flag
    height = width / 15
    result = height
    return result

print(solution())