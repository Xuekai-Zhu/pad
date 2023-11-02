def solution():
    """If one fourth of the engines are defective, and there are 5 batches of 80 engines each. How many engines are not defective?"""
    # Define the fraction of defective engines
    defective_fraction = 1/4

    # Define the total number of engines
    total_engines = 5 * 80

    # Calculate the number of defective engines
    defective_engines = total_engines * defective_fraction

    # Calculate the number of non-defective engines
    non_defective_engines = total_engines - defective_engines

    result = non_defective_engines
    return result

print(solution())