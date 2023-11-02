def solution():
    # Calculate the area of the first two walls
    area1 = 30 * 12
    area2 = 30 * 12
    total_area = area1 + area2

    # Calculate the area of the third wall
    area3 = 20 * 12

    # Add the areas together to get the total area of glass needed
    total_area += area3

    result = total_area
    return result

print(solution())