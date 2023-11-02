def solution():
    """John paints a giant mural that is 6m by 3m. The paint costs $4 per square meter. The artist can paint 1.5 square meters per hour and charges $10 per hour. How much does the mural cost?"""
    # Define the size of the mural
    height = 6
    width = 3

    # Calculate the area of the mural
    area = height * width

    # Calculate the cost of the paint
    paint_cost = area * 4

    # Calculate the time it takes to paint the mural and the cost of labor
    time = area / 1.5  # in hours
    labor_cost = time * 10

    # Calculate the total cost of the mural
    total_cost = paint_cost + labor_cost

    result = total_cost
    return result

print(solution())