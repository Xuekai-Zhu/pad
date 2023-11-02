def solution():
    num_doberman_puppies = 20
    equation_result = 90

    # Calculate the number of Schnauzers
    num_schnauzers = (equation_result - (5 + (3 * num_doberman_puppies))) / 2
    result = num_schnauzers
    return result

print(solution())