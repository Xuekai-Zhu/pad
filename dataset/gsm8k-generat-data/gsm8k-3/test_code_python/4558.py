def solution():
    """Yves and his siblings ordered pizza and asked to have it cut into 16 slices.  During dinner time, they only ate one-fourth of it. The next day, Yves ate one-fourth of the remaining pizza. Then his two siblings ate 2 slices each. How many slices of pizza were left?"""
    # Define the total number of pizza slices
    total_slices = 16

    # Calculate the number of slices eaten during dinner
    dinner_slices = total_slices // 4

    # Calculate the number of remaining slices
    remaining_slices = total_slices - dinner_slices

    # Calculate the number of slices Yves ate the next day
    yves_slices = remaining_slices // 4

    # Calculate the number of remaining slices after Yves ate
    remaining_slices -= yves_slices

    # Calculate the number of slices Yves' siblings ate
    siblings_slices = 2 + 2

    # Calculate the final number of remaining slices
    final_slices = remaining_slices - siblings_slices

    # Display the final number of remaining slices
    result = final_slices
    return result

print(solution())