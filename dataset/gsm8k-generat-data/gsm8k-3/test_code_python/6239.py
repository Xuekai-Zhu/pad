def solution():
    """Vlad is 6 feet, 3 inches tall. His younger sister is 2 feet, 10 inches tall. How many inches taller is Vlad than his sister?"""
    # Define Vlad's and his sister's heights in inches
    VLAD_HEIGHT = (6 * 12) + 3
    SISTER_HEIGHT = (2 * 12) + 10

    # Calculate the height difference in inches
    height_diff = VLAD_HEIGHT - SISTER_HEIGHT

    # Display the height difference in inches
    result = height_diff
    return result

print(solution())