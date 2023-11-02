def solution():
    """Mrs. Kaplan has 1/4 as many pizza slices as Bobby has. If Bobby has 2 pizzas and each pizza has 6 slices, how many slices does Mrs. Kaplan have?"""
    # Calculate the total number of pizza slices Bobby has
    bobby_slices = 2 * 6

    # Calculate the number of slices Mrs. Kaplan has
    kaplan_slices = bobby_slices * (1/4)

    # Display the number of slices Mrs. Kaplan has
    result = kaplan_slices
    return result

print(solution())