def solution():
    # Initialize the number of fish
    num_fish = 2

    # Loop through the 5 years and update the number of fish each year
    for i in range(5):
        num_fish += 1  # add two new fish
        num_fish -= 1  # subtract one dead fish

    result = num_fish
    return result

print(solution())