def solution():
    flour_needed = 6  # cups
    eggs_per_flour = 3/2  # eggs/cup

    # Calculate the total number of eggs needed to make bread with 6 cups of flour
    eggs_needed = flour_needed * eggs_per_flour
    result = eggs_needed
    return result

print(solution())