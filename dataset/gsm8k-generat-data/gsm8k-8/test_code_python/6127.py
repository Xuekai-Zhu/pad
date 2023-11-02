def solution():
    # Define the starting thickness and the number of foldings
    starting_thickness = 3
    num_foldings = 4

    # Double the thickness for each folding
    for i in range(num_foldings):
        starting_thickness *= 2

    result = starting_thickness
    return result

print(solution())