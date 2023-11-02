def solution():
    """Yanni has 5 paintings that combined, take up 200 square feet. 3 of the paintings are 5 feet by 5 feet. 1 painting is 10 feet by 8 feet. If the final painting is 5 feet tall, how wide is it?"""
    # Calculate the total area of the 4 known paintings
    known_paintings_area = 3 * (5 * 5) + (10 * 8)

    # Calculate the area of the fifth painting
    fifth_painting_area = 200 - known_paintings_area

    # Calculate the width of the fifth painting
    fifth_painting_width = fifth_painting_area / 5

    # Return the result
    result = fifth_painting_width
    return result

print(solution())