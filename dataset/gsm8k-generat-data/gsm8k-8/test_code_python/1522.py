def solution():
    # Define the ratio of eggs to flour in the recipe
    eggs_to_flour_ratio = 3/2

    # Determine how many cups of flour the baker will use
    flour_used = 6

    # Calculate how many eggs the baker will need
    eggs_needed = eggs_to_flour_ratio * flour_used
    result = eggs_needed
    return result

print(solution())