def solution():
    initial_thickness = 3  # Janet's blanket starts out 3 inches thick
    num_foldings = 4  # Janet folds her blanket 4 times

    # Calculate the thickness after each folding
    for i in range(num_foldings):
        initial_thickness *= 2

    result = initial_thickness
    return result

print(solution())