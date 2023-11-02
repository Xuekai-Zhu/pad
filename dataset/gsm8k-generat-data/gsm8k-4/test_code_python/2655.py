def solution():
    """Trey is hanging wall decorations around his house. He uses a nail for each of two-thirds of them, a thumbtack for each of two-fifths of the rest, and a sticky strip for each of the other decorations. He used 15 sticky strips. How many nails did Trey use?"""
    # Define the total number of decorations
    total_decorations = None

    # Define the number of decorations that require a sticky strip
    sticky_decorations = 15

    # Calculate the number of decorations that do not require a sticky strip
    non_sticky_decorations = total_decorations - sticky_decorations

    # Calculate the number of decorations that require a thumbtack
    thumbtack_decorations = non_sticky_decorations * (2/5)

    # Calculate the number of decorations that require a nail
    nail_decorations = (non_sticky_decorations - thumbtack_decorations) * (2/3)

    result = int(nail_decorations)
    return result

print(solution())