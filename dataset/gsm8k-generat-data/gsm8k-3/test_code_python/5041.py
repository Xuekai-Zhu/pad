def solution():
    """Yanni has 5 paintings that combined, take up 200 square feet. 3 of the paintings are 5 feet by 5 feet. 1 painting is 10 feet by 8 feet. If the final painting is 5 feet tall, how wide is it?"""
    # Calculate the area of the first three paintings
    area_1 = 3 * (5 * 5)

    # Calculate the area of the fourth painting
    area_2 = 10 * 8

    # Calculate the total area of the first four paintings
    total_area_1 = area_1 + area_2

    # Calculate the remaining area for the fifth painting
    remaining_area = 200 - total_area_1

    # Calculate the width of the fifth painting
    width_5 = remaining_area / 5

    # Display the width of the fifth painting
    result = width_5
    return result

print(solution())