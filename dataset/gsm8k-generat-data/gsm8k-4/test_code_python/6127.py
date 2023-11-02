def solution():
    """Every time Janet folds her blanket its thickness doubles. If it starts out 3 inches thick, how thick will it be after 4 foldings?"""
    # Define the initial thickness and the number of foldings
    initial_thickness = 3
    num_foldings = 4

    # Fold the blanket and double the thickness for each folding
    final_thickness = initial_thickness * (2 ** num_foldings)

    result = final_thickness
    return result

print(solution())