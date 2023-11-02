def solution():
    """Trey is hanging wall decorations around his house. He uses a nail for each of two-thirds of them, a thumbtack for each of two-fifths of the rest, and a sticky strip for each of the other decorations. He used 15 sticky strips. How many nails did Trey use?"""
    # Define the fractions of decorations that require a nail, thumbtack, or sticky strip
    NAIL_FRACTION = 2/3
    THUMBTACK_FRACTION = 2/5
    STICKY_STRIP_FRACTION = 1 - NAIL_FRACTION - THUMBTACK_FRACTION

    # Define the total number of decorations
    total_decorations = 15 / STICKY_STRIP_FRACTION

    # Calculate the number of decorations that require a nail
    nail_decorations = total_decorations * NAIL_FRACTION

    # Display the number of nails used
    result = nail_decorations
    return result

print(solution())