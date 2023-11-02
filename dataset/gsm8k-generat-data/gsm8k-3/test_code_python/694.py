def solution():
    """If one fourth of the engines are defective, and there are 5 batches of 80 engines each. How many engines are not defective?"""
    # Define the proportion of defective engines
    DEFECTIVE_PROPORTION = 1/4

    # Calculate the number of defective engines in one batch
    defective_engines = 80 * DEFECTIVE_PROPORTION

    # Calculate the number of non-defective engines in one batch
    non_defective_engines = 80 - defective_engines

    # Calculate the total number of non-defective engines in all 5 batches
    total_non_defective_engines = non_defective_engines * 5 * 80

    # Display the total number of non-defective engines
    result = total_non_defective_engines
    return result

print(solution())