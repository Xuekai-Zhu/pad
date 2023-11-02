def solution():
    eggs_per_cup_of_flour = 3/2  # The recipe calls for 3 eggs for every 2 cups of flour
    cups_of_flour = 6  # The baker has 6 cups of flour

    # Calculate the number of eggs needed for the 6 cups of flour
    eggs_needed = eggs_per_cup_of_flour * cups_of_flour
    result = eggs_needed
    return result

print(solution())