def solution():
    # Define the initial number of knives and teaspoons
    knives = 24
    teaspoons = 2 * knives

    # Calculate the additional knives and teaspoons
    additional_knives = 1/3 * knives
    additional_teaspoons = 2/3 * teaspoons

    # Calculate the total number of cutlery pieces
    total_cutlery = knives + teaspoons + additional_knives + additional_teaspoons
    result = total_cutlery
    return result

print(solution())